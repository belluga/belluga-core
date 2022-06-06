from pkg_resources import resource_exists
from setuptools import find_packages, setup

setup(name='belluga',
version='0.32',
description='Testing installation of Package',
url='#',
author='auth',
author_email='elton@bellugasolutions.com',
packages=find_packages(),
include_package_data=True,
# license='MIT',
zip_safe=False)