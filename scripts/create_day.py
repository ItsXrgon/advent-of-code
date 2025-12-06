#!/usr/bin/env python3
"""
Create Advent of Code day folders for the current year.

Usage:
    python scripts/create_day.py [DAY]

If DAY is omitted the script uses today's day number.
It creates two folders `DD-1` and `DD-2` under a `YYYY` folder (current year),
and places an empty `input.txt` and a small `main.py` template in each.
"""
from __future__ import annotations

import os
import sys
from datetime import datetime


def make_folder(year_dir: str, day_str: str, part: int) -> bool:
    folder = os.path.join(year_dir, f"{day_str}-{part}")
    created = False
    if not os.path.exists(folder):
        os.makedirs(folder, exist_ok=True)
        created = True

    main_path = os.path.join(folder, "main.py")
    input_path = os.path.join(folder, "input.txt")

    # create an empty python file if it doesn't exist
    if not os.path.exists(main_path):
        with open(main_path, "w", encoding="utf-8") as f:
            f.write(f"# Dec {day_str} 2025 - part {part}\n")
            f.write(f"import time\n\n")
            f.write(f"start_time = time.perf_counter()\n\n")
            f.write(f"file = open('{year_dir}/{day_str}-{part}/input.txt', 'r')\n")
            f.write("\n\n\n\n\n\n\n")
            f.write(f"end_time = time.perf_counter()\n")
            f.write("print(f\"Took {end_time - start_time:.4f} seconds\")")


    # create an empty input file if it doesn't exist
    if not os.path.exists(input_path):
        open(input_path, "w", encoding="utf-8").close()

    return created


def main(argv: list[str] | None = None) -> int:
    if argv is None:
        argv = sys.argv[1:]

    # pick day from arg or today's day
    if len(argv) >= 1:
        try:
            day = int(argv[0])
        except ValueError:
            print("Invalid day number. Provide an integer like: 3 or 03")
            return 2
    else:
        day = datetime.now().day

    # allow optional --year YEAR
    year = datetime.now().year
    if "--year" in argv:
        try:
            yi = argv.index("--year") + 1
            year = int(argv[yi])
        except Exception:
            print("Invalid or missing year after --year")
            return 3

    year_dir = str(year)
    if not os.path.exists(year_dir):
        print(f"Year directory '{year_dir}' not found. Creating it.")
        os.makedirs(year_dir, exist_ok=True)

    day_str = f"{day:02d}"

    created_any = []
    for part in (1, 2):
        created = make_folder(year_dir, day_str, part)
        if created:
            created_any.append(f"{year_dir}/{day_str}-{part}")
        else:
            print(f"Folder '{year_dir}/{day_str}-{part}' already existed; left files as-is.")

    if created_any:
        print("Created folders:")
        for p in created_any:
            print(" -", p)
    else:
        print("No new folders created.")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
