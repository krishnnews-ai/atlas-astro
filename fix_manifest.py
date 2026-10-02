#!/usr/bin/env python3
"""
Fix: Update manifest.json with generated posts (all required fields)
"""
import os
import json

POSTS_DIR = "src/generated/posts"
MANIFEST_FILE = "src/data/manifest.json"

def main():
    print("🔧 Fixing manifest.json...")

    if os.path.exists(MANIFEST_FILE):
        with open(MANIFEST_FILE, "r", encoding="utf-8") as f:
            try:
                manifest = json.load(f)
            except:
                manifest = {}
    else:
        manifest = {}

    if "posts" not in manifest or not isinstance(manifest["posts"], list):
        manifest["posts"] = []
    if "pages" not in manifest or not isinstance(manifest["pages"], list):
        manifest["pages"] = []

    manifest["posts"] = [p for p in manifest["posts"] if isinstance(p, dict)]
    manifest["pages"] = [p for p in manifest["pages"] if isinstance(p, dict)]

    if os.path.exists(POSTS_DIR):
        files = sorted([f for f in os.listdir(POSTS_DIR) if f.endswith(".html")])
        print(f"📁 Found {len(files)} post files")

        # Purani entries hatao, sirf files wali rakho
        existing_slugs = {p.get("slug") for p in manifest["posts"] if p.get("slug")}

        for filename in files:
            slug = filename[:-5]
            title = slug.replace("-", " ").title()

            # Already hai? toh update karo, warna add karo
            found = False
            for p in manifest["posts"]:
                if p.get("slug") == slug:
                    p["title"] = title
                    p["file"] = f"posts/{filename}"
                    p["path"] = f"/{slug}/"
                    p["excerpt"] = p.get("excerpt", "")
                    p["cover"] = p.get("cover", "")
                    p["date"] = p.get("date", "2026-01-01")
                    p["site"] = p.get("site", "CoinAINews")
                    p["categories"] = p.get("categories", ["Crypto"])
                    p["format"] = p.get("format", "standard")
                    p["bodyClass"] = p.get("bodyClass", "single-post")
                    found = True
                    break

            if not found:
                manifest["posts"].append({
                    "slug": slug,
                    "title": title,
                    "excerpt": "",
                    "cover": "",
                    "date": "2026-01-01",
                    "site": "CoinAINews",
                    "categories": ["Crypto"],
                    "format": "standard",
                    "bodyClass": "single-post",
                    "file": f"posts/{filename}",
                    "path": f"/{slug}/"
                })

    os.makedirs(os.path.dirname(MANIFEST_FILE), exist_ok=True)
    with open(MANIFEST_FILE, "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2, ensure_ascii=False)

    print(f"✅ Manifest updated!")
    print(f"   📝 Total posts: {len(manifest['posts'])}")
    print(f"   📄 Total pages: {len(manifest['pages'])}")

if __name__ == "__main__":
    main()
