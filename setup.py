from pathlib import Path
import setuptools
import toml
from os.path import join, dirname, abspath

pyproject_path = join(dirname(abspath("__file__")), '../pyproject.toml')
file = open(pyproject_path, "r")
toml_str = file.read()

home_page = Path(r"https://5395920610@dev.azure.com/5395920610/Inoversity.Library.Microservice")
parsed_toml = toml.loads(toml_str)

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Inoversity Library Microservice",
    version=parsed_toml['tool']['commitizen']['version'],
    author="Mduduzi Mlilo",
    author_email="mduduzi.mlilo@hotmail.com",
    description="Inoversity Library Microservice.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=home_page.joinpath(r"_git/Inoversity.Library.Microservice"),
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.9',
    keywords='pip-demo math',
    project_urls={
        'Homepage': home_page.joinpath(r"_git/Inoversity.Library.Microservice"),
    },
)
