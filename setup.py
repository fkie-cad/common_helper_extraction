from setuptools import find_packages, setup

VERSION = '1.1.0'

setup(
    name='common_helper_extraction',
    version=VERSION,
    packages=find_packages(),
    install_requires=[
        'common_helper_files >= 0.2.2'
    ],
    dependency_links=[
        'git+https://github.com/fkie-cad/common_helper_files.git#egg=common_helper_files-0.2.2',
    ],
    description='Extraction support functions',
    author='Fraunhofer FKIE',
    author_email='firmware-security@fkie.fraunhofer.de',
    url='http://www.fkie.fraunhofer.de',
    license='GPL-3.0'
)
