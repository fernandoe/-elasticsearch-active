from setuptools import setup, find_packages

setup(
    name='elasticsearch-active',
    version='0.0.1',
    description='A simple library to verify if the elastic search service is active',
    packages=find_packages(),
    install_requires=[
        #  'pacote1',
        #  'pacote2'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)

