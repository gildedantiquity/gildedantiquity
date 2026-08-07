# AGENTS.md

## Cursor Cloud specific instructions

This repository is a **GitHub profile README** repo: its only tracked file is `README.md`,
which GitHub renders on the `gildedantiquity` profile page.

- There is **no application code, package manifest, build system, test suite, or linter**.
  Do not expect `package.json`, `requirements.txt`, etc. — none exist and none are needed.
- The update script is intentionally a no-op; there are no dependencies to install.
- To "run" the product, render `README.md` as GitHub-Flavored Markdown and view it in a browser
  (e.g. render to HTML with a Markdown renderer and open it). No repo tooling is required for this.
- The README embeds external badge/stat images (`shields.io`, `github-readme-stats.vercel.app`,
  `github-readme-streak-stats.herokuapp.com`, `komarev.com`). These are third-party services and
  may be temporarily unavailable (e.g. HTTP 503) independent of this environment; broken badge
  images during a preview usually indicate an upstream outage, not a local problem.
