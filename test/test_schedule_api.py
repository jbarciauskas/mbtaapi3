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
from mbtaapi.apis.schedule_api import ScheduleApi


class TestScheduleApi(unittest.TestCase):
    """ ScheduleApi unit test stubs """

    def setUp(self):
        self.api = mbtaapi.apis.schedule_api.ScheduleApi()

    def tearDown(self):
        pass

    def test_api_web_schedule_controller_index(self):
        """
        Test case for api_web_schedule_controller_index

        
        """
        pass


if __name__ == '__main__':
    unittest.main()