from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='twill3',
    version='3.11.18',
    scripts=['twill'],
    packages=find_packages(),
    author='Jon Froiland',
    author_email='jon.froiland@gmail.com',
    description='Update to twill3 for Python3 compatibility',
    long_description='Using 2to3, refactored code for Python3. Version references <Python Version>.<month>.<year>',
    long_description_content_type='text/markdown',
    url='',
    classifiers=[
        'Programming Language :: Python :: 3.6',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
