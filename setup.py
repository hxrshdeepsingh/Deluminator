from pathlib import Path
from setuptools import setup, find_packages

HERE = Path(__file__).parent
README = HERE / "README.md"

setup(
    name="Deluminator",
    version="3.13.21",
    author="Harshdeep Singh",
    author_email="ishu.cxx@gmail.com",
    license="BSD-3-Clause",
    description="Reverse shell generator for Windows systems using sockets.",
    long_description=README.read_text(encoding="utf-8"),
    long_description_content_type="text/markdown",

    packages=find_packages(),

    include_package_data=True,
    package_data={
        "Deluminator.engine": ["source"],
    },

    install_requires=[
        "click",
        "pyinstaller",
        "pyautogui",
    ],

    entry_points={
        "console_scripts": [
            "Deluminator=Deluminator.main:Deluminator",
        ],
    },

    python_requires=">=3.9",
)