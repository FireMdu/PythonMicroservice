from setuptools import setup, find_packages

setup(
   name='LimitRecommendationMicroservice',
   version='0.1',
   packages=find_packages(exclude=['tests']),
   license='MIT',
   long_description="Limit recommendations service",
)
