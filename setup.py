from setuptools import find_packages, setup
import re
import ast

try:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst')
except(IOError, ImportError):
    long_description = open('README.md').read()

_version_re = re.compile(r'__version__\s+=\s+(.*)')

with open('financefeast/__init__.py', 'rb') as f:
    version = str(ast.literal_eval(_version_re.search(
        f.read().decode('utf-8')).group(1)))

setup(
    name='financefeast',
    url="https://github.com/financefeast/python_client",
    packages=find_packages(include=['financefeast']),
    version=version,
    description='A client library for Financefeast API',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Financefeast',
    author_email='support@financefeast.io',
    license='MIT',
    install_requires=['requests'],
    setup_requires=['requests'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests',
    python_requires='>=3.6',
    classifiers = [
                  "Programming Language :: Python :: 3",
                  "License :: OSI Approved :: MIT License",
                  "Operating System :: OS Independent",
              ]
)