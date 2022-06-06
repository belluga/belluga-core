from setuptools import find_packages, setup

setup(name='belluga',
version='0.59',
description='Testing installation of Package',
url='#',
author='auth',
author_email='elton@bellugasolutions.com',
packages=find_packages(),
include_package_data=True,
zip_safe=False,
install_requires=[
    "<fastapi>;python_version<'<0.78.0>'",
    "<uvicorn>;python_version<'<0.17.6>'",
    "<python-decouple>;python_version<'<3.6>'",
    "<fastapi_utils>;python_version<'<0.2.1>'",
    "<motor>;python_version<'<3.0.0>'"
 ]
)