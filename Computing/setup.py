from setuptools import setup, find_packages

setup(
    name='Computing',
    version='1.0.0',
    description='Computing lect using Processing',
    url='https://github.com/BetaFish/jejunu/Computing',
    author='Muhun Kim',
    author_email='iam@muhun.kim',
    keywords='jupyter notebook processing virtualenv pipenv python3.6',
    packages=find_packages(),
    python_requires='>=3',
    install_requires=['jupyter', 'notebook', 'calysto-processing']
)