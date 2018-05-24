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
import envs
import json
import ast
import os
import db_controller
from nso_ui import settings


def add_data_to_db():
    DIR_PATH = os.path.dirname(os.path.realpath(__file__))  # Populate envs with configuration data
    with open(DIR_PATH + '/data/config.json') as data_file:
        json_dict = json.load(data_file)

        print "Saving device types in DB"

        for device_type in db_controller.get_device_types():
            device_type.delete()

        for item in json_dict['device_types']:
            db_controller.add_device_type(name=item['name'])

        print "Saving protocols in DB"
        for protocol in db_controller.get_protocols():
            protocol.delete()
        for item in json_dict['protocols']:
            db_controller.add_protocol(name=item['name'])
