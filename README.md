# zensical-patina

Zensical theme in cyan and amber like copper patina.

Unofficial. Not affiliated with the Zensical project.

## Install

```bash
pip install zensical-patina
```

## Use

```toml
[project.theme]
name = "patina"
```

Optional hero markup:

```html
<div class="patina-hero" markdown>
<p class="patina-kicker">your kicker</p>
# Title
<p class="patina-lede">Lede.</p>
</div>
```

## Preview

```bash
pip install -e .
cd example
zensical serve
```

## Publish

PyPI trusted publishing is wired in `.github/workflows/publish.yml`.
A green push to `main` uploads. Bump `version` in `pyproject.toml` for a
new release; the same version is skipped.
