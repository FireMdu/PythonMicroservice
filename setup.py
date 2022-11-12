from setuptools import setup, find_packages

setup(
   name='InoversityLibraryMicroservice',
   version='1.0.0',
   packages=find_packages(exclude=['tests']),
   license='MIT',
   long_description="Inoversity library management service",
)
