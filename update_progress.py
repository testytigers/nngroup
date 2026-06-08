import os, json, re

with open('progress.json') as f:
    data = json.load(f)

progress_urls = set(u.rstrip('/') for u in data.get('downloaded', []))

# Find all files with nngroup URLs
all_sources = {}
for f in os.listdir('articles'):
    if not f.endswith('.md'):
        continue
    path = os.path.join('articles', f)
    content = open(path, 'r', encoding='utf-8', errors='replace').read()
    urls = re.findall(r'https://www\.nngroup\.com/articles/[^ \n\r"\)<]+', content)
    if urls:
        url = urls[0].rstrip('/')
        all_sources[url] = f

# Find files NOT in progress.json
not_tracked = set(all_sources.keys()) - progress_urls
print(f"Adding {len(not_tracked)} untracked URLs to progress.json")

# Add them
for url in not_tracked:
    if url not in progress_urls:
        data['downloaded'].append(url)

print(f"Total URLs in progress.json now: {len(data['downloaded'])}")

# Save
with open('progress.json', 'w') as f:
    json.dump(data, f, indent=2)

print("Updated progress.json")
