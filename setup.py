from os.path import dirname, join, realpath

from setuptools import find_packages, setup

DESCRIPTION = "Multiple Tools For Experimental Design"
AUTHOR = "John-H-B"
AUTHOR_EMAIL = "113042632+John-H-B@users.noreply.github.com"
URL = "https://github.com/John-H-B/TumTumTree"
LICENSE = "MIT License"

PROJECT_ROOT = dirname(realpath(__file__))

# Get the long description from the README file
with open(join(PROJECT_ROOT, "README.rst"), encoding="utf-8") as buff:
    LONG_DESCRIPTION = buff.read()

REQUIREMENTS_FILE = join(PROJECT_ROOT, "requirements.txt")

with open(REQUIREMENTS_FILE) as f:
    install_reqs = f.read().splitlines()

test_reqs = ["pytest"]

if __name__ == "__main__":
    setup(
        name="tumtumtree",
        maintainer=AUTHOR,
        maintainer_email=AUTHOR_EMAIL,
        description=DESCRIPTION,
        license=LICENSE,
        url=URL,
        long_description=LONG_DESCRIPTION,
        long_description_content_type="text/x-rst",
        packages=find_packages(exclude=["tests*"]),
        python_requires=">=3.8",
        install_requires=install_reqs,
        tests_require=test_reqs,
    )