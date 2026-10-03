#!/usr/bin/env python3
import json, os, re

MANIFEST = "src/data/manifest.json"
POSTS_DIR = "src/generated/posts"

def get_cover(slug):
    path = os.path.join(POSTS_DIR, f"{slug}.html")
    if not os.path.exists(path):
        return ""
    try:
        html = open(path, encoding="utf-8").read()
        m = re.search(r'<img[^>]+src=["\']([^"\']+)["\']', html)
        return m.group(1) if m else ""
    except:
        return ""

def main():
    if not os.path.exists(MANIFEST):
        print(f"❌ {MANIFEST} not found")
        return
    if os.path.getsize(MANIFEST) == 0:
        print(f"❌ {MANIFEST} is empty")
        return

    with open(MANIFEST, encoding="utf-8") as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError as e:
            print(f"❌ Invalid JSON: {e}")
            return

    count = 0
    for post in data.get("posts", []):
        if not post.get("cover"):
            cover = get_cover(post["slug"])
            if cover:
                post["cover"] = cover
                count += 1

    with open(MANIFEST, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"✅ {count} posts me cover add hua")

if __name__ == "__main__":
    main()
