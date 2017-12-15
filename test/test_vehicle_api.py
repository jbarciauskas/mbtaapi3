# coding: utf-8

"""
    MBTA

    MBTA service API. https://www.mbta.com

    OpenAPI spec version: 3.0
    Contact: developer@mbta.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import mbtaapi
from mbtaapi.rest import ApiException
from mbtaapi.apis.vehicle_api import VehicleApi


class TestVehicleApi(unittest.TestCase):
    """ VehicleApi unit test stubs """

    def setUp(self):
        self.api = mbtaapi.apis.vehicle_api.VehicleApi()

    def tearDown(self):
        pass

    def test_api_web_vehicle_controller_index(self):
        """
        Test case for api_web_vehicle_controller_index

        
        """
        pass

    def test_api_web_vehicle_controller_show(self):
        """
        Test case for api_web_vehicle_controller_show

        
        """
        pass


if __name__ == '__main__':
    unittest.main()