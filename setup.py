from setuptools import setup, find_packages

VERSION = '0.2'

setup(
    name='common_helper_extraction',
    version=VERSION,
    packages=find_packages(),
    install_requires=[
        'common_helper_extraction'
    ],
    description='Extraction support functions',
    author='Fraunhofer FKIE',
    author_email='firmware-security@fkie.fraunhofer.de',
    url='http://www.fkie.fraunhofer.de',
    license='GPL-3.0'
)
