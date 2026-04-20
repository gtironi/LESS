import io
from setuptools import setup, find_packages 
import pathlib
with pathlib.Path('requirement.txt').open() as f:
    install_requires = [line.strip() for line in f if line.strip() and not line.startswith('#')]


setup(
    name='less',
    packages=["less"],
    version='0.1',
    description='LESS',
    author='Mengzhou Xia',
    url='https://github.com/princeton-nlp/LESS',
    install_requires=install_requires,
    entry_points={
        "console_scripts": [],
    },
    package_data={},
    classifiers=["Programming Language :: Python :: 3"],
)
