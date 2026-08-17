---
icon: lucide/book-open
---

# Usage

The PyPI package is `zensical-patina`. The theme name is `patina`.

## Install

```bash
pip install zensical-patina
```

Requires Python 3.10 or newer.

## Configure

```toml
[project]
site_name = "Patina"

[project.theme]
name = "patina"
```

Optional hero markup (needs `md_in_html`):

```html
<div class="patina-hero" markdown>
<p class="patina-kicker">your kicker</p>
# Title
<p class="patina-lede">Lede.</p>
</div>
```

## Local preview

From a clone of this repository:

```bash
pip install -e .
cd example
zensical serve
```
