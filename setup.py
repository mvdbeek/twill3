from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='twill',
    version='1.9.0',
    scripts=['twill-sh'],
    packages=find_packages(),
    author='C. Titus Brown and Ben R. Taylor',
    author_email='titus@idyll.org',
    license='MIT',
    description='twill Web browsing language',
    long_description='A scripting system for automating Web browsing. Useful for testing Web pages or grabbing data from password-protected sites automatically.',
    long_description_content_type='text/markdown',
    url='https://github.com/ctb/twill',
    classifiers=[
        'Programming Language :: Python :: 3.6',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ], install_requires=['lxml', 'cssselect', 'requests', 'pyparsing']
)
