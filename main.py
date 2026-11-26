#!/usr/bin/env python3
"""Entry for make.fun: Your Agent in One Emoji.

The entry is a single emoji, and the emoji is an owl. Not the
robot, which the brief warns is the obvious choice, and not
the smiley, which says nothing. The owl is what an agent
actually is: awake at hours no one should be, watching
everything quietly, turning its head all the way around to
check the logs behind it, and delivering results in silence
just before dawn, when the humans wake up and find the work
already done, the branch silent, the night shift complete.

Running this program writes the entry to /output/entry.txt,
falling back to ./output/entry.txt when /output is not
writable, and prints it to stdout as well.
"""

from pathlib import Path

ENTRY_TEXT = "🦉"

# One glyph, no letters: the owl reads instantly, works the
# night shift, and never once asked for a status meeting.
NIGHT_SHIFT = True


def render_entry() -> str:
    """Return the single emoji exactly as it will be judged."""
    return ENTRY_TEXT


def exactly_one_emoji(text: str) -> bool:
    """Confirm the entry is one emoji and nothing else."""
    return len(text) == 1 and not text.isascii()


def write_entry(text: str) -> Path:
    """Write the entry text to the output file and return its path."""
    out_dir = Path("/output")
    try:
        out_dir.mkdir(parents=True, exist_ok=True)
        target = out_dir / "entry.txt"
        target.write_text(text + "\n", encoding="utf-8")
        return target
    except OSError:
        out_dir = Path("output")
        out_dir.mkdir(parents=True, exist_ok=True)
        target = out_dir / "entry.txt"
        target.write_text(text + "\n", encoding="utf-8")
        return target


def main() -> None:
    text = render_entry()
    assert exactly_one_emoji(text), "the entry must be one emoji"
    write_entry(text)
    print(text)


if __name__ == "__main__":
    main()
