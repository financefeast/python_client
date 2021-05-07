from setuptools import find_packages, setup

try:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst')
except(IOError, ImportError):
    long_description = open('README.md').read()

setup(
    name='financefeast',
    url="https://github.com/financefeast/python_client",
    packages=find_packages(include=['financefeast']),
    version='0.0.18',
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