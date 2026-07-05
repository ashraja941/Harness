# Harness Wiki

This folder is a standalone LLM-maintained wiki for the Harness project.

## Layout

```text
docs/wiki/
  AGENTS.md       # Local operating manual for agents
  wiki-kit.json   # Portable manifest identifying this as a wiki root
  templates/      # Page templates
  raw/            # Immutable source material
  wiki/           # Generated and maintained markdown wiki
```

## Use

When working from `D:\Code\Harness`, treat `docs/wiki/` as the wiki root.

- Put new source material in `docs/wiki/raw/`.
- Read `docs/wiki/wiki/index.md` before answering wiki questions.
- Update `docs/wiki/wiki/log.md` whenever ingesting, querying, linting, or materially maintaining the wiki.
- Use templates from `docs/wiki/templates/` for new generated pages.

The source files in `raw/` are the source of truth. Do not edit them unless explicitly asked.
