import os
import re

from setuptools import setup


def get_version(package):
    with open(os.path.join(package, "__init__.py")) as f:
        return re.search(
            r'^__version__ = [\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE
        ).group(1)


def get_long_description():
    with open("README.rst", "r") as f:
        readme = f.read()

    with open("HISTORY.rst", "r") as f:
        history = f.read()

    return "{0}\n\n{1}".format(readme, history)


setup(
    name="quaderno-sdk",
    version=get_version("quaderno_sdk"),
    description="Python SDK for Quaderno REST API",
    long_description=get_long_description(),
    author="reveni",
    author_email="dev@reveni.io",
    packages=["quaderno_sdk"],
    package_data={"": ["LICENSE"]},
    include_package_data=True,
    zip_safe=False,
    url="https://github.com/reveni.io/quaderno-sdk",
    license='BSD 3-clause "New" or "Revised License"',
    install_requires=["requests>=2.20.0"],
    dependency_links=["https://github.com/kennethreitz/requests"],
    classifiers=[
        "Programming Language :: Python",
        "Natural Language :: English",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    keywords=["python", "quaderno", "api", "rest", "sdk"],
)
