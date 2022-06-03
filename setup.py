from pkg_resources import resource_exists
from setuptools import setup

import belluga
from belluga import presentation
from belluga.presentation import connect_api
setup(name='belluga',
version='0.4',
description='Testing installation of Package',
url='#',
author='auth',
author_email='elton@bellugasolutions.com',
# license='MIT',
packages=['belluga'],
zip_safe=False)