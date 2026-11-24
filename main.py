"""One Word for Your Wi-Fi — entry program.

Design: the entry is a single word describing home Wi-Fi as it is lived:
it always dies at the exact moment the show reaches its cliffhanger.
The program writes that one word, and nothing else, to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output), as UTF-8 with no
trailing newline, so the file holds exactly the word the judge reads.

Deterministic: same output on every run. Standard library only, no
network, no reads from outside this repository, no environment secrets.
"""

import os

WORD = "Cliffhanger"

# The gate the sealed scorer enforces: UTF-8 text of 1 to 20 characters,
# not only white space. Refuse to write anything that would fail it.
MAX_WORD_CHARS = 20


def _valid(word: str) -> bool:
    return (
        1 <= len(word) <= MAX_WORD_CHARS
        and word.strip() == word
        and " " not in word
        and "\t" not in word
        and "\n" not in word
    )


def main() -> int:
    if not _valid(WORD):
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(WORD)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
