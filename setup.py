from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='crosslinked',
    version='0.3.1',
    author='Borghese-Gladiator',
    license='GPLv3',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/Borghese-Gladiator/CrossLinked',
    packages=find_packages(include=[
        "crosslinked", "crosslinked.*"
    ]),
    install_requires=[
        'beautifulsoup4',
        'bs4',
        'certifi',
        'charset-normalizer',
        'idna',
        'lxml',
        'requests',
        'soupsieve',
        'Unidecode',
        'urllib3'
    ],
    classifiers=[
        "Environment :: Console",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Topic :: Security"
    ],
    entry_points={
        'console_scripts': ['crosslinked=crosslinked:main']
    }
)