from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='pyhumour',
    version='0.0.1',
    description='A module for the characterization and quantification of concise humour',
    py_modules=["pyhumour"],  # list of files that can be imported
    package_dir={'': 'pyhumour'},
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: GNU General Public License v2 or later (GPLv3+)",
        "Operating System :: OS Independent"
    ],
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=[
        "numpy ~= 1.17"
    ],
    extras_require = {
        "dev": [
            "pytest>=5.4",
            "twine>=3.1"
        ]
    },
    url="https://github.com/mellon-collie/pyhumour",
    author='Unscholars',
    author_email='prjctstuff@gmail.com',
)
