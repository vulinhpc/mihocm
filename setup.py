from pathlib import Path

from setuptools import find_packages, setup

with Path(__file__).resolve().parent.joinpath("requirements.txt").open() as requirements_file:
    install_requires = [line.strip() for line in requirements_file if line.strip() and not line.startswith("#")]

from mihocm import __version__  # noqa: E402

setup(
    name="mihocm",
    version=__version__,
    description="Miho construction management",
    author="Linh Vu",
    author_email="mrlinhvu1987@gmail.com",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=install_requires,
)
