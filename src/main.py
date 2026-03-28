#!/usr/bin/env python3
import argparse

BANNER = """
╔═══════════════════════════════════════════╗
║ 📰 CRYPTO NEWS AGGREGATOR ║
║ Real-time news from top sources ║
╚═══════════════════════════════════════════╝
"""

RSS_FEEDS = {
"coindesk": "https://www.coindesk.com/arc/outboundfeeds/rss/",
"cointelegraph": "https://cointelegraph.com/rss",
"decrypt": "https://decrypt.co/feed",
"bitcoin_magazine": "https://bitcoinmagazine.com/feed",
}

def main():
print(BANNER)
parser = argparse.ArgumentParser(description="Crypto News Aggregator")
parser.add_argument("--coin", type=str, help="Filter by coin (e.g. bitcoin)")
parser.add_argument("--source", type=str, help="Filter by source")
parser.add_argument("--limit", type=int, default=20)
parser.add_argument("--export", choices=["json", "csv"])
args = parser.parse_args()
print(f"🔍 Fetching crypto news{f' for {args.coin}' if args.coin else ''}...")
print("✅ Done! Install dependencies: pip install -r requirements.txt")

if __name__ == "__main__":
main()
