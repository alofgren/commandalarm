import setuptools
import commandalarm

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="CommandAlarm",
    version=commandalarm.__version__,
    author="alofgren",
    author_email="drelofren@outlook.com",
    description=("A simple command line program that allows users to set"
                 " an alarm with a custom command."),
    license="GPLv3+",
    keywords=[
        "alarm", "command", "command-line", "tool", "timer", "commandalarm"
    ],
    url="https://github.com/alofgren/commandalarm",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    entry_points={
        "console_scripts": ["commandalarm = commandalarm.commandalarm:main"]
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: Implementation :: CPython",
        "Topic :: Utilities",
    ],
    project_urls={
        "Source":
        "https://github.com/alofgren/commandalarm",
        "Bug Reports":
        "https://github.com/alofgren/commandalarm/issues",
        "Changelog":
        "https://github.com/alofgren/commandalarm/blob/main/CHANGELOG.md",
    },
    python_requires=">=3.7",
)
