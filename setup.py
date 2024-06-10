# -*- coding: utf-8 -*-
from setuptools import setup, find_packages


setup(
    name='darksearch',
    version="1.3",
    packages=find_packages(),
    author="megadose",
    install_requires=["requests","argparse","termcolor","tqdm", "html5lib","bs4","PySocks"],
    description="darkSearch is a script that scrapes urls on different .onion search engines.",
    include_package_data=True,
    url='https://github.com/slashinvestigator/Darksearch',
    entry_points = {'console_scripts': ['darksearch = darksearch.core:scrape']},
    classifiers=[
        "Programming Language :: Python",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
)
