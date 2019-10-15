import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

long_description += "```python3"
with open("sample/sample.py", "r") as fh:
    long_description += fh.read()
long_description += "```"

setuptools.setup(
    name="getthat",
    version="0.0.2",
    author="Erdem Aybek",
    author_email="eaybek@gmail.com",
    description=" ".join(
        [
            "getthat i dont care if i don't have it.\n"
            "(pip3 install if modulenotfound)"
        ]
    ),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/eaybek/getthat",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
        "Development Status :: 1 - Planning",
    ],
    python_requires=">=3.6",
)
