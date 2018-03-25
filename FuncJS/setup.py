from setuptools import setup, find_packages

setup(
    name='FuncJS',
    version='1.0.0',
    description='Functional JavaScript Practice',
    url='https://github.com/BetaFish/jejunu',
    author='Muhun Kim',
    author_email='iam@muhun.kim',
    keywords='jupyter notebook virtualenv pipenv python3.6',
    packages=find_packages(),
    python_requires='>=3',
    install_requires=['jupyter', 'notebook']
)