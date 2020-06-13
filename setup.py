# v0.1.6 released
from setuptools import setup, find_packages

setup(name="graphrepo",
      version="0.1.6",
      description="A tool that maps a Github repo to Neo4j and Helps Mining the Repo in the DB",
      url="https://github.com/NullConvergence/GraphRepo",
      license='Apache License',
      python_requires='>=3.5',
      packages=find_packages(),
      package_dir={'graphrepo': 'graphrepo'})
