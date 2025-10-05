from __future__ import annotations

from pathlib import Path
from pkgutil import extend_path

__path__ = list(extend_path(__path__, __name__))

_inner = Path(__file__).resolve().parent / "mihocm"
if _inner.is_dir():
    inner_path = str(_inner)
    if inner_path not in __path__:
        __path__.append(inner_path)
    about: dict[str, str] = {}
    version_file = _inner / "__init__.py"
    if version_file.exists():
        exec(version_file.read_text(encoding="utf-8"), about)
    __version__ = about.get("__version__", "0.0.1")
else:
    __version__ = "0.0.1"

__all__ = []
