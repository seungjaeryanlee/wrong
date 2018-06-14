import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="wrong",
    version="0.0.0",
    author="Seung Jae (Ryan) Lee",
    author_email="seungjaeryanlee@gmail.com",
    description="Evaluate your unit test skills",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/seungjaeryanlee/wrong",
    packages=setuptools.find_packages(exclude=['tests']),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)