import os, json, re

with open('progress.json') as f:
    data = json.load(f)
tracked = set(u.rstrip('/') for u in data.get('downloaded', []))

# Scrape the main nngroup.com site to find ALL article URLs
import urllib.request

def fetch_page(url):
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)'})
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            return resp.read().decode('utf-8')
    except Exception as e:
        return None

# Get the sitemap or main pages to find article URLs
print("Fetching nngroup.com sitemap...")
sitemap = fetch_page('https://www.nngroup.com/sitemap.xml')
if sitemap:
    # Extract URLs from sitemap
    sitemap_urls = re.findall(r'<loc>(https://www\.nngroup\.com/articles/[^<]+)</loc>', sitemap)
    sitemap_urls = [u.rstrip('/') for u in sitemap_urls]
    print(f"Found {len(sitemap_urls)} article URLs in sitemap")
    
    missing = [u for u in sitemap_urls if u not in tracked]
    print(f"Articles NOT yet downloaded: {len(missing)}")
    print(f"\nFirst 20 missing:")
    for u in missing[:20]:
        print(f"  {u}")
    
    if missing:
        # Save missing URLs to a file for scraping
        with open('missing_urls.txt', 'w') as f:
            for u in missing:
                f.write(u + '\n')
        print(f"\nSaved {len(missing)} missing URLs to missing_urls.txt")
else:
    print("Could not fetch sitemap, trying main page...")
    # Try fetching main page
    main = fetch_page('https://www.nngroup.com/')
    if main:
        # Find all article links
        article_urls = re.findall(r'href="(https://www\.nngroup\.com/articles/[^"]+)"', main)
        article_urls = [u.rstrip('/') for u in article_urls]
        print(f"Found {len(article_urls)} article URLs on main page")
        
        missing = [u for u in article_urls if u not in tracked]
        print(f"Articles NOT yet downloaded: {len(missing)}")
        for u in missing[:20]:
            print(f"  {u}")
