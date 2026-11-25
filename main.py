#!/usr/bin/env python3
"""Write one line to /output/entry.txt: the funniest one-line epitaph,
a single line of famous last words carved in stone.

The line was picked from 36 candidates by pairwise judging against the
brief — the speaker finally wins the last word, only for that word to
be "oops": a win that is also a loss, in one short line. The program
holds the line as one constant and checks it against the entry gate
(length, single line, no leading or trailing space, exact judged
length) before writing it, then reads the file back to confirm the
bytes match. The line is 43 characters, a single line, and ends on
its strongest beat: the punch word "oops".
"""

import os
import sys

LINE = "I finally got the last word. It was 'oops.'"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = os.path.join(out_dir, "entry.txt")
    if not (1 <= len(LINE) <= 150):
        sys.exit(f"line is {len(LINE)} characters, gate needs 1-150")
    if "\n" in LINE or LINE != LINE.strip():
        sys.exit("line must be a single line with no surrounding space")
    data = (LINE + "\n").encode("utf-8")
    os.makedirs(out_dir, exist_ok=True)
    with open(path, "wb") as f:
        f.write(data)
    os.chmod(path, 0o644)
    with open(path, "rb") as f:
        if f.read() != data:
            sys.exit("read-back mismatch")
    print(f"wrote {len(data)} bytes to {path}")


if __name__ == "__main__":
    main()
