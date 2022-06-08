from setuptools import find_packages, setup

setup(name='belluga',
version='1.1.15',
description='Testing installation of Package',
url='#',
author='auth',
author_email='elton@bellugasolutions.com',
packages=find_packages(),
include_package_data=True,
zip_safe=False,
install_requires=[
    "fastapi>=0.78.0",
    "uvicorn>=0.17.6",
    "python-decouple>=3.6",
    "fastapi_utils>=0.2.1",
    "pymongo[srv]>=4.1.1"
 ]
)