#!/usr/bin/env python3
"""Generate up to N Hugo posts for a given date from internal/posting-schedule.json.

Editorial schedule stays internal; only rendered Markdown under site/content/posts is public.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parents[1]
SCHEDULE_PATH = ROOT / "internal" / "posting-schedule.json"
POSTS_DIR = ROOT / "site" / "content" / "posts"
DEFAULT_TZ = "Asia/Jakarta"
DEFAULT_COUNT = 3


def slugify(value: str) -> str:
    value = value.lower().strip()
    value = re.sub(r"[^a-z0-9\s-]", "", value)
    value = re.sub(r"[\s_]+", "-", value)
    return re.sub(r"-{2,}", "-", value).strip("-")


def load_schedule() -> dict:
    if not SCHEDULE_PATH.exists():
        raise FileNotFoundError(f"Missing schedule: {SCHEDULE_PATH}")
    return json.loads(SCHEDULE_PATH.read_text(encoding="utf-8"))


def existing_slugs() -> set[str]:
    if not POSTS_DIR.exists():
        return set()
    return {p.stem for p in POSTS_DIR.glob("*.md") if p.name != "_index.md"}


def pick_topics(schedule: dict, day: str, count: int) -> list[dict]:
    """Only create posts scheduled for this exact day (do not steal future slots)."""
    posts = schedule.get("posts", [])
    have = existing_slugs()
    for_day = [
        p
        for p in posts
        if p.get("date") == day and p.get("slug") and p["slug"] not in have
    ]
    # Preserve schedule order, limit to count
    return for_day[:count]


def estimate_reading_time(sections: list[dict]) -> int:
    words = 180
    for section in sections:
        words += 40 + 25 * len(section.get("points", []))
    return max(5, min(12, round(words / 160)))


def render_section(section: dict) -> str:
    heading = section["heading"]
    points = section.get("points") or []
    intro = section.get("intro") or (
        f"Berikut ringkasan praktis untuk bagian **{heading}** yang bisa langsung Anda terapkan."
    )
    lines = [f"## {heading}", "", intro, ""]
    if points:
        for point in points:
            lines.append(f"- {point}")
        lines.append("")
    takeaway = section.get("takeaway")
    if takeaway:
        lines.extend([takeaway, ""])
    return "\n".join(lines)


def render_post(topic: dict, day: str, tz_name: str) -> str:
    title = topic["title"]
    slug = topic.get("slug") or slugify(title)
    theme = topic.get("theme") or "Umum"
    summary = topic.get("summary") or title
    lede = topic.get("lede") or summary
    sections = topic.get("sections") or [
        {
            "heading": "Konteks masalah",
            "intro": f"Topik ini penting karena {summary[0].lower() + summary[1:] if summary else 'sering muncul di otomasi agen'}.",
            "points": [
                "Tentukan outcome yang ingin dicapai sebelum memilih pola agen.",
                "Pisahkan bagian yang cukup digarap rule engine dari bagian yang butuh reasoning.",
                "Catat asumsi dan data yang belum tersedia agar loop tidak mengarang.",
            ],
            "takeaway": "Mulai dari batasan masalah yang sempit; perluas hanya setelah metrik dasar stabil.",
        },
        {
            "heading": "Pola yang direkomendasikan",
            "intro": f"Untuk tema {theme}, pakai pola yang mudah diaudit dan punya stop condition jelas.",
            "points": [
                "Definisikan input, tools, dan kriteria selesai secara eksplisit.",
                "Batasi iterasi, biaya, dan aksi berbahaya dengan policy.",
                "Simpan jejak keputusan agar kegagalan bisa di-replay.",
            ],
        },
        {
            "heading": "Checklist implementasi",
            "intro": "Sebelum men-ship otomasi ini ke produksi, pastikan poin berikut sudah tercentang.",
            "points": [
                "Ada allowlist tools dan uji skenario gagal.",
                "Ada human-in-the-loop untuk aksi destruktif.",
                "Ada metrik sukses, latensi, dan biaya per tugas.",
                "Ada fallback bila model/tool tidak tersedia.",
            ],
        },
    ]

    reading = topic.get("readingTime") or estimate_reading_time(sections)
    dt = datetime.fromisoformat(f"{day}T08:00:00").replace(tzinfo=ZoneInfo(tz_name))
    date_str = dt.isoformat()

    body_parts = [render_section(section) for section in sections]
    body_parts.append(
        "## Penutup\n\n"
        f"Ringkasnya: {summary} Jadikan ini satu eksperimen kecil hari ini, ukur hasilnya, "
        "lalu baru skala.\n"
    )

    front_matter = "\n".join(
        [
            "---",
            f'title: "{title.replace(chr(34), chr(39))}"',
            f"date: {date_str}",
            "draft: false",
            f"theme: {theme}",
            f"readingTime: {reading}",
            f'lede: "{lede.replace(chr(34), chr(39))}"',
            f'generated_by: "scripts/generate_daily_posts.py"',
            "---",
            "",
        ]
    )
    return front_matter + "\n".join(body_parts), slug


def write_posts(topics: list[dict], day: str, tz_name: str, dry_run: bool) -> list[Path]:
    POSTS_DIR.mkdir(parents=True, exist_ok=True)
    written: list[Path] = []
    for topic in topics:
        content, slug = render_post(topic, day, tz_name)
        path = POSTS_DIR / f"{slug}.md"
        if path.exists():
            print(f"skip existing {path.relative_to(ROOT)}", file=sys.stderr)
            continue
        if dry_run:
            print(f"dry-run would write {path.relative_to(ROOT)}")
            written.append(path)
            continue
        path.write_text(content, encoding="utf-8")
        print(f"wrote {path.relative_to(ROOT)}")
        written.append(path)
    return written


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--date",
        help="Target date YYYY-MM-DD (default: today in schedule timezone)",
    )
    parser.add_argument(
        "--count",
        type=int,
        default=None,
        help="How many posts to create (default: schedule.posts_per_day or 3)",
    )
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    schedule = load_schedule()
    tz_name = schedule.get("timezone") or DEFAULT_TZ
    count = args.count or int(schedule.get("posts_per_day") or DEFAULT_COUNT)
    day = args.date or datetime.now(ZoneInfo(tz_name)).date().isoformat()

    topics = pick_topics(schedule, day, count)
    if not topics:
        print(f"No pending topics for {day}; nothing to do.")
        return 0

    print(f"Generating {len(topics)} post(s) for {day} ({tz_name})")
    written = write_posts(topics, day, tz_name, args.dry_run)
    print(f"created={len(written)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
