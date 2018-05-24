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

Main access for environmental variables. The values in this file represent default values and can only be changed
using the config_files/config.json file. You will need to restart the app to apply those changes

"""

import os

__author__ = "Santiago Flores Kanter (sfloresk@cisco.com)"


def get_username():
    return os.getenv("USERNAME", "")


def get_password():
    return os.getenv("PASSWORD", "")


def get_nso_user():
    return os.getenv("NSO_USER", "")


def get_nso_password():
    return os.getenv("NSO_PASS", "")


def get_nso_ip():
    return os.getenv("NSO_IP", "")


def get_nso_netconf_port():
    return os.getenv("NSO_NETCONF_PORT", "")


def get_nso_rest_port():
    return os.getenv("NSO_REST_PORT", "")


def get_nso_server_user():
    """
    User from the linux server where NSO is running
    :return:
    """
    return os.getenv("NSO_SERVER_USER", "")


def get_nso_server_password():
    """
    Password from the linux server where NSO is running
    :return:
    """
    return os.getenv("NSO_SERVER_PASSWORD", "")


def get_nso_packages_dir():
    """
    Password from the linux server where NSO is running
    :return:
    """
    return os.getenv("NSO_PACKAGES_DIR", "")


def get_db_svc():
    return os.getenv("DB_SVC", "")


def get_db_port():
    return os.getenv("DB_PORT", "")


def get_db_name():
    return os.getenv("DB_NAME", "nso_ui")


def get_db_user():
    return os.getenv("DB_USER", "")


def get_db_password():
    return os.getenv("DB_PASSWORD", "")


def get_db_type():
    return os.getenv("DB_TYPE", "")



