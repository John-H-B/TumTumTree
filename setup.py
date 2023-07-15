from setuptools import find_packages, setup

DESCRIPTION = "Multiple Tools For Experimental Design"


with open('requirements.txt') as r_file:
    requirements = r_file.read().rstrip('\x00')

if __name__ == "__main__":
    print(requirements)
    print(type(requirements))
    setup(
        name="tumtumtree",
        description=DESCRIPTION,
        packages=find_packages(exclude=["tests*"]),
        install_requires=requirements,
    )