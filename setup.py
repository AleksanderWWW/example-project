from setuptools import (
    find_packages,
    setup,
)

if __name__ == "__main__":
    requirements = ["requests"]
    setup(install_requires=requirements, packages=find_packages(where="src"), package_dir={"": "src"}, zip_safe=False)
