from setuptools import find_packages, setup

setup(
    name="Dundie", 
    version="0.1.0",
    description="Teste 2 Teste",
    author="Charles Bambineti",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "dundie = dundie.__main__:main"
        ]
    }
)