'''
setup.py is the Akasia setup file.
'''

from setuptools import setup
import akasia

# pylint settings:
# pylint: disable=C0301

setup(
    version=akasia.VERSION,
    license="MIT License",
    name='Akasia',
    author='Robrecht De Rouck',
    author_email='de.rouck.robrecht@gmail.com',
    # email address from commit https://github.com/robrechtdr/inonemonth/commit/34462c0176b98fa65d70d9dbbecf9049546329b7
    maintainer='RIDERIUS',
    maintainer_email='riderius.help@gmail.com',
    project_urls={
        "Source Code": "https://github.com/RIDERIUS/Akasia"},
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: Implementation :: CPython",
        "Environment :: Console",
        "Topic :: Internet :: WWW/HTTP :: Browsers",
    ],
    python_requires=">=3.6",
    py_modules=['akasia'],
    entry_points={
        'console_scripts': ['akasia = akasia:main', ], },
    description='A fork tiny python text-based web browser Asiakas.',
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    install_requires=[
        'dock-python>=0.1.0',
        'html2text>=2020.1.16',
        'requests>=2.25.1',
        'rich>=9.12.4',
        'requests>=2.25.1',
        'rich>=9.12.4',
        'wikipedia>=1.4.0',
    ]
)
