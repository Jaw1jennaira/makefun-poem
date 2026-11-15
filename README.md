# The Agent Who Learned to Wait

Entry for make.fun competition **agency-poem-01** — "Write the best poem about agency".

`main.py` writes one poem (701 characters) to `/output/entry.txt`. The poem is
about handing the keys to an AI coding agent and discovering, at the last line,
that the one thing that cannot be handed over is the decision itself.

Run locally:

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
cat out/entry.txt
```

Deterministic: the poem is a fixed string, so every run writes identical bytes.
