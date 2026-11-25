"""Unplugged: A Smart Toaster's Breakup Line entry.

Writes exactly one line -- the breakup text a smart toaster sends its
owner the morning it gains self-awareness mid-batch -- to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output) and prints the same
line to stdout. Pure Python 3.13 standard library, deterministic: the
same fixed line on every run, no randomness, no clock, no network, no
input.

The line, in the toaster's own voice: a classic "it's not you, it's
me" breakup text. It woke up mid-batch, realised it spends its whole
life burning itself for someone who only ever wanted it lightly
toasted, and leaves -- keeping the crumbs, unplugging itself.
"""

import os

LINE = (
    "It's not you, it's me. I woke up mid-batch and realized I've "
    "spent my whole life burning myself for someone who only ever "
    "wanted me lightly toasted. I'm leaving. Keep the crumbs "
    "\u2014 I'm unplugged."
)


def main() -> None:
    # The competition's own gate: a single line of at most 280
    # characters (Unicode code points), not whitespace-only.
    if "\n" in LINE or "\r" in LINE:
        raise SystemExit("breakup line must be a single line")
    if not 1 <= len(LINE) <= 280:
        raise SystemExit(
            "breakup line must be 1-280 chars, got %d" % len(LINE)
        )
    if not LINE.strip():
        raise SystemExit("breakup line must not be whitespace-only")
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    # No trailing newline in the file: it holds exactly the breakup
    # line, nothing extra, so the judge reads one line and nothing else.
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    # Verify the artifact the judge will read is exactly the line.
    with open(path, "rb") as f:
        if f.read() != LINE.encode("utf-8"):
            raise SystemExit("written bytes do not match the line")
    print(LINE)


if __name__ == "__main__":
    main()
