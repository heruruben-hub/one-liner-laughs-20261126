"""One-Liner Laughs entry.

Writes a single funny line — a real one-line joke — to
/output/entry.txt (UTF-8, one line, no trailing newline).
"""

import os

LINE = "I finally bought a standing desk so I can procrastinate upright, like a professional."


def _validate(line: str) -> None:
    """Check the line against the competition gate: 1-200 chars, one line."""
    if not 1 <= len(line) <= 200:
        raise ValueError("entry must be 1-200 characters")
    if not line.strip() or "\n" in line or "\r" in line:
        raise ValueError("entry must be a single non-blank line")


def _write_and_verify(line: str) -> None:
    """Write the line to /output/entry.txt and verify the written bytes."""
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(line)
    with open("/output/entry.txt", "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != line:
        raise ValueError("written entry does not match the joke")


def main() -> None:
    _validate(LINE)
    _write_and_verify(LINE)


if __name__ == "__main__":
    main()
