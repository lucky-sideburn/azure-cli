#---------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#---------------------------------------------------------------------------------------------
#pylint: skip-file
# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator 0.16.0.0
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class StorageAccountBaseProperties(Model):
    """StorageAccountBaseProperties

    :param name:
    :type name: str
    """ 

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
    }

    def __init__(self, name=None):
        self.name = name