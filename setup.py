import os

from setuptools import (
    find_packages,
    setup,
)

if __name__ == "__main__":
    root_dir = os.path.dirname(__file__)
    with open(os.path.join(root_dir, "requirements.txt")) as f:
        requirements = [r.strip() for r in f]

    setup(install_requires=requirements, packages=find_packages(where="src"), package_dir={"": "src"})
