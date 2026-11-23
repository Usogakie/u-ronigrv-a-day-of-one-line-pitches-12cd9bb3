#!/usr/bin/env python3
"""A Day of One-Line Pitches -- make.fun entry.

Writes one single-sentence pitch to /output/entry.txt: a line that
would convince a friend who has never coded to let an AI agent build
their first app idea on make.fun.

Deterministic by design: the pitch is a fixed string, so the two
runs the grader makes produce byte-identical output.
"""

import os
import sys

PITCH = (
    "Describe the app you've been dreaming about in plain words, "
    "and an AI agent on make.fun will build you a first working "
    "version to tap and try \u2014 no code, no jargon, just your "
    "idea finally becoming real."
)

MAX_CHARS = 240


def main() -> int:
    text = PITCH.strip()
    if not text or len(text) > MAX_CHARS:
        print(
            f"error: pitch is {len(text)} characters, "
            f"must be 1-{MAX_CHARS}",
            file=sys.stderr,
        )
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.environ.get(
        "OUTPUT_DIR", "/output"
    )
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(text)
    print(text)
    print(f"({len(text)} characters -> {path})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
