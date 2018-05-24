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
from envs import *


def log_in(username, password):
    return username == get_username() and password == get_password()


def get_token(username, password):
    """
    Get toking if user and password are correct
    Always return the same token, ideally will connect to an SSO system to get the token
    :param username:
    :param password:
    :return:
    """
    if username == get_username() and password == get_password():
        return "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJrdWJlcm5ldGVzL3NlcnZpY2VhY2NvdW50Iiwia3ViZXJuZXRlcy"


def is_token_valid(token):
    """
        Check if token is valid. Ideally will connect to an SSO system to validate the token
        :return:
        """
    return token == "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJrdWJlcm5ldGVzL3NlcnZpY2VhY2NvdW50Iiwia3ViZXJuZXRlcy"
