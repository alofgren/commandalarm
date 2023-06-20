import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup (
    name = "CommandAlarm",
    version = "0.2.6",
    author = "alofgren",
    author_email = "drelofren@outlook.com",
    description = "A simple command line program that allows users to set an alarm with a custom command.",
    license = "GPLv3",
    keywords = ["alarm","command","command-line","tool","timer","commandalarm"],
    url = "https://github.com/alofgren/commandalarm",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    packages = setuptools.find_packages(),
    entry_points = {
        "console_scripts": [
            "commandalarm = commandalarm.commandalarm:main"
        ]
    },
    classifiers = [
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Intended Audience :: End Users/Desktop",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Topic :: Utilities",
    ],
    project_urls = {
        "Bug Reports": "https://github.com/alofgren/commandalarm/issues",
        "Source": "https://github.com/alofgren/commandalarm",
    },
    python_requires = ">=3"
)
