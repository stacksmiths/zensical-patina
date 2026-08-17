from importlib.metadata import entry_points
from pathlib import Path

import patina


def test_theme_entry_point() -> None:
    names = {ep.name for ep in entry_points(group="mkdocs.themes")}
    assert "patina" in names


def test_theme_files() -> None:
    root = Path(patina.__file__).resolve().parent
    assert (root / "mkdocs_theme.yml").is_file()
    assert (root / "main.html").is_file()
    assert (root / "assets" / "stylesheets" / "patina.css").is_file()
