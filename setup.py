from __future__ import annotations

from pathlib import Path
from typing import List

from setuptools import find_packages, setup

ROOT = Path(__file__).resolve().parent


def read_requirements() -> List[str]:
    requirements_path = ROOT / "requirements.txt"
    if not requirements_path.exists():
        return []

    return [
        line.strip()
        for line in requirements_path.read_text(encoding="utf-8").splitlines()
        if line.strip() and not line.lstrip().startswith("#")
    ]


def read_version() -> str:
    about: dict[str, str] = {}
    version_file = ROOT / "mihocm" / "__init__.py"
    exec(version_file.read_text(encoding="utf-8"), about)
    return about["__version__"]


setup(
    name="mihocm",
    version=read_version(),
    description="Miho construction management",
    author="Linh Vu",
    author_email="mrlinhvu1987@gmail.com",
    packages=find_packages(include=["mihocm", "mihocm.*"]),
    include_package_data=True,
    zip_safe=False,
    install_requires=read_requirements(),
)
