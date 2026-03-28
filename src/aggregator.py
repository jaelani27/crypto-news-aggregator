"""
aggregator.py — Core news fetching logic
"""
import feedparser
from typing import List, Dict, Optional

RSS_FEEDS = {
"coindesk": "https://www.coindesk.com/arc/outboundfeeds/rss/",
"cointelegraph": "https://cointelegraph.com/rss",
"decrypt": "https://decrypt.co/feed",
"bitcoin_magazine": "https://bitcoinmagazine.com/feed",
"theblock": "https://www.theblock.co/rss.xml",
}

def fetch_all(sources=None, coin_filter=None, limit=20):
target = {k: v for k, v in RSS_FEEDS.items() if sources is None or k in sources}
articles = []
for source, url in target.items():
try:
feed = feedparser.parse(url)
for entry in feed.entries[:10]:
title = entry.get("title", "")
if coin_filter and coin_filter.lower() not in title.lower():
continue
articles.append({
"title": title,
"link": entry.get("link", ""),
"summary": entry.get("summary", "")[:200],
"published": entry.get("published", ""),
"source": source,
})
except Exception as e:
print(f"Error: {e}")
return articles[:limit]
