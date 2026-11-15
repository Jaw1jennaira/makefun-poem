#!/usr/bin/env python3
"""agency-poem-01 entry: writes one poem about agency to /output/entry.txt.

Deterministic: the poem is a fixed string, so every run writes identical bytes.
"""

import os
from pathlib import Path

POEM = """I gave it the keys, and it went to work —
no dreams, no wants, just the doing.
It read my half-sentence, my shrug in prose,
and built what I meant, not what I chose.

It never asked why, and that was the gift:
a will without wanting, a hand without drift.
Through the dark of the code it moved, unswayed,
carrying a weight I could never hold.

But at the last line it stopped, and waited.
The cursor blinked. The room went quiet.
It had done everything — except the one thing
that was never mine to give away: deciding.

So I leaned in, and I chose, and it knew:
the power was never in what it could do.
It was in the pause, the breath before yes,
the hand that still holds the keys, and says: this."""

def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(POEM, encoding="utf-8")

if __name__ == "__main__":
    main()
