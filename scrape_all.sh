#!/bin/bash
# Wrapper: keeps running scrape_remaining.py until all articles are downloaded
cd /Users/yahya/Desktop/nngroup

TOTAL_IN_SITEMAP=1710
GOAL=$((TOTAL_IN_SITEMAP - 885))  # URLs still needed = total - already in progress.json

echo "Goal: download $GOAL articles (to reach $TOTAL_IN_SITEMAP total)"
echo "---"

RUN=0
while true; do
    RUN=$((RUN + 1))
    BEFORE=$(ls articles/*.md 2>/dev/null | wc -l)
    echo "Run $RUN: $(date +%H:%M:%S) — $(ls articles/*.md 2>/dev/null | wc -l) files on disk, $(python3 -c "import json; d=json.load(open('progress.json')); print(len(d.get('downloaded',[])))") URLs in progress.json"
    echo "---"
    
    PYTHONUNBUFFERED=1 python3 scrape_remaining.py 2>&1 | tail -5
    
    AFTER=$(ls articles/*.md 2>/dev/null | wc -l)
    URLS=$(python3 -c "import json; d=json.load(open('progress.json')); print(len(d.get('downloaded',[])))")
    
    echo "After run $RUN: $AFTER files, $URLS URLs"
    echo "=== DONE ==="
    break
done
