#!/usr/bin/env python3
"""The 3 AM Excuse - make.fun entry.

Writes one original line - the excuse a hardware wallet gives for
refusing to sign a transaction at 3 AM - to /output/entry.txt
(or $MAKEFUN_OUTPUT_DIR/entry.txt), then prints it.
"""

import os
import sys

EXCUSE = "No. At 3 AM I don't sign anything \u2014 my only job is standing between you and the worst decision of your financial life."

MAX_CHARS = 200


def main() -> int:
    line = EXCUSE
    if not line or line != line.strip():
        print("error: excuse must be one non-blank line", file=sys.stderr)
        return 1
    if "\n" in line or "\r" in line:
        print("error: excuse must be a single line", file=sys.stderr)
        return 1
    if len(line) > MAX_CHARS:
        print(
            f"error: excuse is {len(line)} characters, "
            f"over the {MAX_CHARS} limit",
            file=sys.stderr,
        )
        return 1
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(line + "\n")
    print(line)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
