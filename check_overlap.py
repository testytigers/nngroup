import os, json, re

with open('progress.json') as f:
    data = json.load(f)
progress_urls = set(u.rstrip('/') for u in data.get('downloaded', []))

# Find all files with nngroup URLs
all_sources = {}
no_sources = []
for f in os.listdir('articles'):
    if not f.endswith('.md'):
        continue
    path = os.path.join('articles', f)
    content = open(path, 'r', encoding='utf-8', errors='replace').read()
    # Find all nngroup article URLs in the file
    urls = re.findall(r'https://www\.nngroup\.com/articles/[^ \n\r"\)<]+', content)
    if urls:
        # Take the first one
        url = urls[0].rstrip('/')
        all_sources[url] = f
    else:
        no_sources.append(f)

# Check overlap
overlap = set(all_sources.keys()) & progress_urls
not_in_progress = set(all_sources.keys()) - progress_urls
extra_in_progress = progress_urls - set(all_sources.keys())

print(f"Files with nnG URLs: {len(all_sources)}")
print(f"Files without nnG URLs: {len(no_sources)}")
print(f"Overlap with progress.json: {len(overlap)}")
print(f"NOT in progress.json: {len(not_in_progress)}")
print(f"URLs in progress.json with no file: {len(extra_in_progress)}")

# Show untracked files (in disk but not in progress.json)
if not_in_progress:
    print(f"\nFirst 10 files NOT in progress.json:")
    for url in sorted(not_in_progress)[:10]:
        print(f"  {url} -> {all_sources[url]}")

# Show files in progress.json without files on disk
if extra_in_progress:
    print(f"\nFirst 10 URLs in progress.json with NO file:")
    for url in sorted(extra_in_progress)[:10]:
        print(f"  {url}")
