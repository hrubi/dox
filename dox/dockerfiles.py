# Copyright (c) 2016 GoodData
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

__all__ = [
    'get_dockerfiles',
]

import os

import dox.config.dox_yaml
import dox.config.tox_ini


class Dockerfile(str):
    pass


def get_dockerfiles(options):
    '''Examine the local environment and figure out where we should run.'''

    dox_yaml = dox.config.dox_yaml.get_dox_yaml(options)
    tox_ini = dox.config.tox_ini.get_tox_ini(options)

    default_dockerfile = 'Dockerfile'

    dockerfiles = []
    if dox_yaml.exists():
        dockerfiles = dox_yaml.get_dockerfiles()
    elif tox_ini.exists():
        dockerfiles = tox_ini.get_dockerfiles()
    elif os.path.exists(default_dockerfile):
        dockerfiles = [default_dockerfile]

    if not dockerfiles:
        return None

    return [Dockerfile(dockerfile) for dockerfile in dockerfiles]
