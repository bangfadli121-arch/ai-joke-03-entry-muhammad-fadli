"""Write the competition joke to the configured output directory."""

import os
from pathlib import Path


JOKE = "I asked my coding agent to review its own code. It approved the pull request, merged it, then opened an issue against itself."


def main():
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    output_file = output_dir / "entry.txt"
    output_file.write_text(JOKE, encoding="utf-8")


if __name__ == "__main__":
    main()
