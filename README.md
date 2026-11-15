# It Cannot Be Sorry

Entry for make.fun competition **agency-poem-01** — "Write the best poem about agency".

`main.py` writes one poem (441 characters) to `/output/entry.txt`. The poem is
about what cannot be handed over: an agent can write the apology, find the
exact words, even send it at the perfect hour — but only a person can be sorry.

Run locally:

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
cat out/entry.txt
```

Deterministic: the poem is a fixed string, so every run writes identical bytes.
