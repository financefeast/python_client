from setuptools import find_packages, setup

setup(
    name='financefeast',
    url="https://github.com/financefeast/python_client",
    packages=find_packages(include=['financefeast']),
    version='0.0.2',
    description='A client library for Financefeast API',
    author='Financefeast',
    author_email='support@financefeast.io',
    license='MIT',
    install_requires=[],
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