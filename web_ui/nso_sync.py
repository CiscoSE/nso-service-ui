"""
Copyright (c) 2018 Cisco and/or its affiliates.

This software is licensed to you under the terms of the Cisco Sample
Code License, Version 1.0 (the "License"). You may obtain a copy of the
License at

               https://developer.cisco.com/docs/licenses

All use of the material herein must be in accordance with the terms of
the License. All rights not expressly granted by the License are
reserved. Unless required by applicable law or agreed to separately in
writing, software distributed under the License is distributed on an "AS
IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
or implied.

"""
"""
Initial config for the application

"""

import db_controller
from api_controller import ApiPackagesNSO
import envs


def sync():
    print "Getting package definitions from NSO:"
    nso_packages_controller = ApiPackagesNSO(envs.get_nso_server_user(), envs.get_nso_server_password(),
                                             envs.get_nso_ip())

    for ned in db_controller.get_neds():
        ned.delete()

    data = nso_packages_controller.get_packages()

    print "Services loaded:"
    print data
