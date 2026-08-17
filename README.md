# zensical-patina

[![CI](https://github.com/stacksmiths/zensical-patina/actions/workflows/ci.yml/badge.svg)](https://github.com/stacksmiths/zensical-patina/actions/workflows/ci.yml)
[![Publish](https://github.com/stacksmiths/zensical-patina/actions/workflows/publish.yml/badge.svg)](https://github.com/stacksmiths/zensical-patina/actions/workflows/publish.yml)
[![PyPI](https://img.shields.io/pypi/v/zensical-patina)](https://pypi.org/project/zensical-patina/)
[![Python](https://img.shields.io/pypi/pyversions/zensical-patina)](https://pypi.org/project/zensical-patina/)

Zensical theme in cyan and amber like copper patina.

Unofficial. Not affiliated with the Zensical project.

**[Live demo](https://stacksmiths.github.io/zensical-patina/)**

## Install

```bash
pip install zensical-patina
```

Requires Python 3.10–3.14.

## Use

The package name is `zensical-patina`. The theme name is `patina`.

```toml
[project.theme]
name = "patina"
```

Optional hero markup (enable `md_in_html`):

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

The `example/` site is the live demo. GitHub Pages deploys it from `main`.

## Publish

A green push to `main` uploads to PyPI via trusted publishing. Bump
`version` in `pyproject.toml` for a new release; the same version is skipped.

## License

MIT. See [LICENSE](LICENSE).
