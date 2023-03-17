from setuptools import setup, find_packages

setup(
    name="testcli",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "debugpy",
        "Click",
        "Click-plugins",
        "pyyaml",
    ],
    entry_points={
        "console_scripts": [
            "testcli = src.cli:testcli",
        ],
    },
    extras_require={"development": ["mypy", "black[d]", "flake8", "pytest", "devtools"]},
)