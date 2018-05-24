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
Database models for app
"""
from models import *
import requests
import json
import authentication
from envs import *

__author__ = "Santiago Flores Kanter (sfloresk@cisco.com)"

"""******** Generics ********"""


def save_entity(entity):
    return entity.save()


"""******** NEDs ********"""


def get_neds(**db_filter):
    return NED.objects.all().filter(**db_filter)


def get_first_ned(**db_filters):
    m_list = NED.objects.all().filter(**db_filters)
    if len(m_list) == 0:
        return None
    return m_list[0]


def add_ned(**kwargs):
    return NED(**kwargs).save()


def delete_ned(ned_id):
    m_list = NED.objects.filter(ned_id=ned_id)
    if len(m_list) == 1:
        m_list[0].delete()
    else:
        raise Exception("Not existing model or not unique identifier")


"""******** Protocols ********"""


def get_protocols(**db_filter):
    return Protocol.objects.all().filter(**db_filter)


def get_first_protocol(**db_filters):
    m_list = Protocol.objects.all().filter(**db_filters)
    if len(m_list) == 0:
        return None
    return m_list[0]


def add_protocol(**kwargs):
    return Protocol(**kwargs).save()


def delete_protocol(protocol_id):
    m_list = Protocol.objects.filter(id=protocol_id)
    if len(m_list) == 1:
        m_list[0].delete()
    else:
        raise Exception("Not existing model or not unique identifier")


"""******** DeviceTypes ********"""


def get_device_types(**db_filter):
    return DeviceType.objects.all().filter(**db_filter)


def get_first_device_type(**db_filters):
    m_list = DeviceType.objects.all().filter(**db_filters)
    if len(m_list) == 0:
        return None
    return m_list[0]


def add_device_type(**kwargs):
    return DeviceType(**kwargs).save()


def delete_device_type(device_type_id):
    m_list = DeviceType.objects.filter(id=device_type_id)
    if len(m_list) == 1:
        m_list[0].delete()
    else:
        raise Exception("Not existing model or not unique identifier")
