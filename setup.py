# coding: utf-8

# Copyright (c) 2016 "Hugo Herter http://hugoherter.com"
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#  http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from setuptools import setup

setup(name='hereby',
      version='0.3.1',
      description='Small Python library for accessing files in the same folder as your code',
      #long_description=open('README.rst').read(),
      author='Hugo Herter',
      author_email='@hugoherter.com',
      url='https://github.com/hoh/Here/',
      py_modules=['hereby'],
      scripts=['hereby.py'],
      license='Apache License 2.0',
      keywords="open relative module file template",
      classifiers=['Development Status :: 3 - Alpha',
                   'Programming Language :: Python :: 2',
                   'Programming Language :: Python :: 3',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: Apache Software License',
                   'Topic :: Software Development :: Libraries',
                   'Topic :: Utilities',
                   ],
      )
