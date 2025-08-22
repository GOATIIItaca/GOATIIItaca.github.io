#!/usr/bin/env python3
import csv
from pathlib import Path

TEMPLATE = """---
layout: redirect
redirect_to: "{target}"
permalink: /{slug}
---

Redirecting to <a href="{target}">{target}</a>
"""

def main(csv_path, out_dir):
    out = Path(out_dir)
    out.mkdir(exist_ok=True)
    with open(csv_path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            slug = row['slug'].strip()
            target = row['target_url'].strip()
            file = out / f"{slug}.md"
            file.write_text(TEMPLATE.format(slug=slug, target=target),
                            encoding='utf-8')
            print(f"Created {file}")

if __name__ == "__main__":
    import argparse
    p = argparse.ArgumentParser()
    p.add_argument("csv", help="Path to redirects.csv")
    p.add_argument("out", help="Output folder (e.g., _redirects)")
    args = p.parse_args()
    main(args.csv, args.out)
