#!/usr/bin/env python3
"""
Automatically assign categories to posts based on title keywords.
"""
import json
import re
import os

MANIFEST_FILE = "src/data/manifest.json"

# Category rules — order matters (first match wins)
CATEGORY_RULES = [
    ("Bitcoin News", [
        "bitcoin", "btc", "satoshi", "saylor", "strategy", "microstrategy",
        "blackrock bitcoin", "bitcoin etf"
    ]),
    ("Ethereum News", [
        "ethereum", " eth ", "vitalik", "ether ", "eth etf", "staking eth"
    ]),
    ("Stablecoin", [
        "stablecoin", "usdt", "usdc", "tether", "usd coin", "dai", "fdusd",
        "rlusd", "usde", "stable coin"
    ]),
    ("Wallet", [
        "wallet", "metamask", "ledger", "seed", "custody", "private key",
        "coldcard", "safepal", "trust wallet", "hardware wallet", "self-custody"
    ]),
    ("Crypto Regulations", [
        " sec ", "cftc", "regulation", "clarity act", "law ", "senate",
        "congress", "bill ", "mica", "legal", "court", "lawsuit", "compliance",
        "tax ", "irs ", "government", "policy", "trump", "white house",
        "eu ", "esma", "imf", "ban ", "license"
    ]),
    ("Altcoin News", [
        "solana", "xrp", "cardano", " bnb", "memecoin", "altcoin",
        "dogecoin", "shiba", "ripple", "monero", "zcash", "litecoin",
        "avalanche", "polkadot", "tron", "ton ", "near ", "aptos", "sui ",
        "chainlink", "uniswap", "aave", "arbitrum", "optimism", "base "
    ]),
    ("Market News", [
        "market", "price", "surge", "crash", "rally", "bull", "bear",
        "etf", "inflow", "outflow", "trading", "volume", "liquidation",
        "futures", "options", "derivative", "whale", "dump", "pump",
        "resistance", "support", "analysis", "forecast", "prediction",
        "kalshi", "cme", "grayscale", "fidelity", "vanguard"
    ]),
    ("Editor's Choice", [
        " ai ", "agent", "chatgpt", "openai", "anthropic", "nvidia",
        "artificial intelligence", "machine learning", "superintelligence",
        "ai model", "ai agent", "gpt", "claude", "gemini"
    ]),
]

def assign_category(title: str) -> str:
    title_lower = " " + title.lower() + " "
    
    for cat, keywords in CATEGORY_RULES:
        for kw in keywords:
            if kw in title_lower:
                return cat
    
    # Default
    return "Market News"

def main():
    print("🔧 Loading manifest...")
    
    if not os.path.exists(MANIFEST_FILE):
        print(f"❌ {MANIFEST_FILE} not found")
        return
    
    with open(MANIFEST_FILE, "r", encoding="utf-8") as f:
        manifest = json.load(f)
    
    if "posts" not in manifest:
        print("❌ No posts in manifest")
        return
    
    updated = 0
    category_counts = {}
    
    for post in manifest["posts"]:
        # Skip if post already has a non-default category
        current_cats = post.get("categories", [])
        
        # Check if already has a real category
        has_real_cat = any(
            c and c.lower() not in ["crypto", "coinai news", ""]
            for c in current_cats
        )
        
        if has_real_cat:
            continue
        
        # Assign new category based on title
        new_cat = assign_category(post.get("title", ""))
        post["categories"] = [new_cat]
        updated += 1
        
        category_counts[new_cat] = category_counts.get(new_cat, 0) + 1
    
    with open(MANIFEST_FILE, "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2, ensure_ascii=False)
    
    print(f"✅ Updated {updated} posts")
    print("\n📊 Category distribution:")
    for cat, count in sorted(category_counts.items(), key=lambda x: -x[1]):
        print(f"   {cat}: {count}")

if __name__ == "__main__":
    main()
