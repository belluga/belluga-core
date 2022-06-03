from pkg_resources import resource_exists
from setuptools import find_packages, setup

import belluga
from belluga import presentation
from belluga.presentation import connect_api
setup(name='belluga',
version='0.5',
description='Testing installation of Package',
url='#',
author='auth',
author_email='elton@bellugasolutions.com',
packages=find_packages(),
include_package_data=True,
# license='MIT',
packages=['belluga'],
zip_safe=False)