#!/usr/bin/env python3
"""
NN/g article scraper — downloads all missing articles from the sitemap.
Downloads .md files into ~/Desktop/nngroup/articles/
Updates ~/Desktop/nngroup/progress.json
"""

import json
import os
import re
import time
import urllib.request
import urllib.error
from pathlib import Path

ARTICLES_DIR = Path(os.path.expanduser("~/Desktop/nngroup/articles"))
PROGRESS_FILE = Path(os.path.expanduser("~/Desktop/nngroup/progress.json"))
SITEMAP_URL = "https://www.nngroup.com/sitemap.xml"
REQUEST_TIMEOUT = 15
RATE_LIMIT = 0.8  # seconds between requests
RETRY_DELAY = 3  # seconds between retries

# Words that stay lowercase in titles (like title case rules)
LOWER_CASE_WORDS = {
    'a', 'an', 'the', 'and', 'or', 'but', 'for', 'nor', 'so', 'yet',
    'of', 'to', 'in', 'on', 'at', 'by', 'up', 'out', 'if', 'is', 'as',
    'it', 'its', 'this', 'that', 'with', 'from', 'into', 'onto',
}


def slug_to_filename(slug):
    """Convert URL slug to filename matching existing convention.
    E.g. '10-best-intranets-of-2023-what-makes-them-great'
         -> '10-Best-Intranets-of-2023-What-Makes-Them-Great.md'
    """
    words = slug.split("-")
    formatted = []
    for i, w in enumerate(words):
        if w.isdigit():
            formatted.append(w)
        elif w.lower() in LOWER_CASE_WORDS and i > 0:
            formatted.append(w.lower())
        elif w.lower() in LOWER_CASE_WORDS and i == 0:
            # First word always capitalized even if it's an article
            formatted.append(w.capitalize())
        else:
            formatted.append(w.capitalize())
    return "-".join(formatted) + ".md"


def parse_sitemap(url):
    """Download and parse the sitemap XML, return article URLs and their dates."""
    print(f"Downloading sitemap...")
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=REQUEST_TIMEOUT) as resp:
        xml = resp.read().decode("utf-8")

    # Extract article URLs with lastmod dates
    urls = {}
    # Parse consecutive <url> blocks
    url_blocks = re.findall(r'<url>(.*?)</url>', xml, re.DOTALL)
    for block in url_blocks:
        loc_match = re.search(r'<loc>(https://www\.nngroup\.com/articles/[^/]+/)</loc>', block)
        mod_match = re.search(r'<lastmod>(\d{4}-\d{2}-\d{2})</lastmod>', block)
        if loc_match:
            urls[loc_match.group(1)] = mod_match.group(1) if mod_match else None

    print(f"  Found {len(urls)} article URLs in sitemap")
    return urls


def get_existing_filenames():
    """Get set of already downloaded filenames."""
    if not ARTICLES_DIR.exists():
        return set()
    return {f.name for f in ARTICLES_DIR.iterdir() if f.is_file()}


def download_article(url, filename):
    """Download an article page and save as markdown."""
    filepath = ARTICLES_DIR / filename
    if filepath.exists():
        return True, "already exists"

    retries = 3
    for attempt in range(retries):
        try:
            req = urllib.request.Request(url, headers={
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36",
                "Accept": "text/html,application/xhtml+xml",
                "Accept-Language": "en-US,en;q=0.9",
            })
            with urllib.request.urlopen(req, timeout=REQUEST_TIMEOUT) as resp:
                html = resp.read().decode("utf-8")

            # Extract title from HTML
            title_match = re.search(r'<title>(.*?)</title>', html, re.IGNORECASE)
            title = title_match.group(1).strip() if title_match else filename.replace(".md", "")

            # Extract article body — NN/g articles have content in article tags
            body_match = re.search(r'<article[^>]*>(.*?)</article>', html, re.DOTALL | re.IGNORECASE)
            if not body_match:
                body_match = re.search(r'class="article-body"[^>]*>(.*?)</div>', html, re.DOTALL | re.IGNORECASE)
            if not body_match:
                body_match = re.search(r'class="post-content"[^>]*>(.*?)</div>', html, re.DOTALL | re.IGNORECASE)

            if body_match:
                content = body_match.group(1)
            else:
                # Strip all tags
                content = re.sub(r'<script[^>]*>.*?</script>', '', html, flags=re.DOTALL | re.IGNORECASE)
                content = re.sub(r'<style[^>]*>.*?</style>', '', content, flags=re.DOTALL | re.IGNORECASE)
                content = re.sub(r'<[^>]+>', '\n', content)

            # Clean up whitespace
            lines = [line.strip() for line in content.splitlines() if line.strip()]
            content_text = '\n\n'.join(lines)
            content_text = re.sub(r'\n{3,}', '\n\n', content_text)

            md_content = f"# {title}\n\n{content_text}"
            filepath.write_text(md_content, encoding="utf-8")
            return True, "downloaded"

        except (urllib.error.HTTPError, urllib.error.URLError) as e:
            if attempt < retries - 1:
                print(f"    ⚠️ Retry {attempt+1}/{retries} for {filename}")
                time.sleep(RETRY_DELAY)
                continue
            return False, str(e)
        except Exception as e:
            return False, str(e)

    return False, "max retries exceeded"


def main():
    # 1. Load existing progress
    downloaded_urls = set()
    if PROGRESS_FILE.exists():
        try:
            with open(PROGRESS_FILE) as f:
                data = json.load(f)
            downloaded_urls = set(data.get("downloaded", data)) if isinstance(data, dict) else set(data)
        except:
            pass

    print(f"Already in progress.json: {len(downloaded_urls)} URLs")

    # 2. Get existing filenames
    existing_files = get_existing_filenames()
    print(f"Files on disk: {len(existing_files)}")

    # 3. Download sitemap
    sitemap_urls = parse_sitemap(SITEMAP_URL)

    # 4. Find missing URLs (in sitemap but not in progress)
    # Normalize URLs by stripping trailing slashes for comparison
    downloaded_normalized = set(u.rstrip('/') for u in downloaded_urls)
    sitemap_normalized = {u.rstrip('/'): u for u in sitemap_urls.keys()}
    missing_urls = set(sitemap_normalized.keys()) - downloaded_normalized
    print(f"\nMissing articles: {len(missing_urls)}")

    if not missing_urls:
        print("\n✅ All articles already in progress.json!")
        return

    # 5. Sort by date (newest first)
    missing_sorted = sorted(missing_urls, key=lambda u: sitemap_urls.get(u, "0000-00-00"), reverse=True)

    # 6. Download
    success_count = 0
    fail_count = 0
    skip_count = 0
    downloaded_list = list(downloaded_urls)

    print(f"\n{'='*60}")
    print(f"Starting download of {len(missing_sorted)} articles...")
    print(f"{'='*60}\n")

    for i, url in enumerate(missing_sorted):
        filename = slug_to_filename(url.rstrip("/").split("/")[-1])
        
        # Skip if file already exists on disk
        if filename in existing_files:
            skip_count += 1
            downloaded_urls.add(url)
            downloaded_list.append(url)
            continue

        ok, status = download_article(url, filename)

        if ok:
            success_count += 1
            downloaded_urls.add(url)
            downloaded_list.append(url)
            prefix = "✅"
        else:
            fail_count += 1
            prefix = "❌"

        # Progress every 50 (also saves progress.json for crash recovery)
        if (i + 1) % 50 == 0 or (i + 1) == len(missing_sorted):
            print(f"[{i+1}/{len(missing_sorted)}] ✅{success_count}  ❌{fail_count}  ⏭️{skip_count}")
            # Save partial progress for recovery
            progress_data = {
                "downloaded": sorted(set(downloaded_list)),
                "completed_at": time.strftime("%Y-%m-%d %H:%M:%S"),
                "stats": {
                    "total_in_sitemap": len(sitemap_urls),
                    "newly_downloaded": success_count,
                    "failures": fail_count,
                    "skipped_existing": skip_count,
                }
            }
            with open(PROGRESS_FILE, "w") as f:
                json.dump(progress_data, f, indent=2)

        time.sleep(RATE_LIMIT)

    # 7. Save progress
    progress_data = {
        "downloaded": sorted(set(downloaded_list)),
        "completed_at": time.strftime("%Y-%m-%d %H:%M:%S"),
        "stats": {
            "total_in_sitemap": len(sitemap_urls),
            "newly_downloaded": success_count,
            "failures": fail_count,
            "skipped_existing": skip_count,
        }
    }
    with open(PROGRESS_FILE, "w") as f:
        json.dump(progress_data, f, indent=2)

    # 8. Final stats
    final_files = len(list(ARTICLES_DIR.iterdir()))

    print(f"\n{'='*60}")
    print(f"COMPLETE!")
    print(f"  Newly downloaded: {success_count}")
    print(f"  Failures: {fail_count}")
    print(f"  Skipped (already on disk): {skip_count}")
    print(f"  Total files on disk: {final_files}")
    print(f"  Total URLs in progress: {len(progress_data['downloaded'])}")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()
