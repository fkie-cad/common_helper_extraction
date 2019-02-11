from setuptools import setup, find_packages

VERSION = '0.4'

setup(
    name='common_helper_extraction',
    version=VERSION,
    packages=find_packages(),
    install_requires=[
        'common_helper_files >= 0.2'
    ],
    dependency_links=[
        'https://github.com/fkie-cad/common_helper_files/tarball/master#egg=common_helper_files-0.2',
    ],
    description='Extraction support functions',
    author='Fraunhofer FKIE',
    author_email='firmware-security@fkie.fraunhofer.de',
    url='http://www.fkie.fraunhofer.de',
    license='GPL-3.0'
)
