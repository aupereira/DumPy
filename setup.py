from setuptools import find_packages, setup

setup(
    name='lamepy',
    packages=find_packages(include=['dumpy']),
    version='0.1.0',
    description='A garbage Python package that does some math',
    author='Aurora Pereira',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_reuire=['pytest==4.4.1'],
    test_suite='tests'
)