import os
from setuptools import find_packages, setup


def read(*path):
    rootpath = os.path.dirname(__file__)
    filepath = os.path.join(rootpath, *path)
    with open(filepath) as file_:
        return file_.read().strip()


def read_requirements(path):
    return [
        line.strip()
        for line in read(path).split("\n")
        if not line.startswith(("#", "git+", '"', '-'))
    ]


setup(
    name="Dundie", 
    version="0.1.0",
    description="Teste 2 Teste",
    long_description=read("README.md"),
    long_description_conten_type="text/markdown",
    author="Charles Bambineti",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "dundie = dundie.__main__:main"
        ]
    },
    install_requires=read_requirements("requirements.txt"),
    extras_requires={
        "test": read_requirements("requirements.test.txt"),
        "dev": read_requirements("requirements.dev.txt"),
    }
)
