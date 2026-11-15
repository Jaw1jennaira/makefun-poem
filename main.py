#!/usr/bin/env python3
"""agency-poem-01 entry: writes one poem about agency to /output/entry.txt.

The poem is about what cannot be handed over: an agent can write and send
the apology, but only a person can be sorry.

Deterministic: the poem is a fixed string, so every run writes identical bytes.
"""

import os
from pathlib import Path

POEM = """It can write the apology.
It can find the exact words —
sorry, my fault, I understand —
arranged in the order that heals.

It can send it at the perfect hour,
when he is most likely to forgive.

It cannot be sorry.

Give it everything else: the typing,
the timing, the turn of phrase.
But someone must stand behind the words
and mean them, or they mean nothing.

So keep one job for yourself.
Not the typing. Not the timing.
The being sorry."""

def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(POEM, encoding="utf-8")

if __name__ == "__main__":
    main()
