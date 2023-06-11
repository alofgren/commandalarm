import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="CommandAlarm",
    version="0.2.4",
    author="alofgren",
    author_email="drelofren@outlook.com",
    description="A simple command line program that allows users to set an alarm with a custom command.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/alofgren/commandalarm",
    packages=setuptools.find_packages(),
    entry_points={
        "console_scripts": [
            "commandalarm=commandalarm.commandalarm:main"
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
    ],
    python_requires = ">=3"
)
