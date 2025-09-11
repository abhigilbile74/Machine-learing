from setuptools import setup, find_packages

def parse_requirements(filename):
    """Load requirements from a requirements.txt file"""
    with open(filename) as f:
        return f.read().splitlines()

setup(
    name="machine_learning_project",
    version="0.1.0",
    author="Abhi Gilbile",
    author_email="abhigilbile74@gmail.com",
    description="A machine learning project for experiments",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/abhigilbile74/Machine-learing",
    packages=find_packages(),
    install_requires=parse_requirements("requirements.txt"),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)
