# coding: utf-8

"""
    Compute Job Manager

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.1.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import compute_api_client
from compute_api_client.models.final_result import FinalResult  # noqa: E501
from compute_api_client.rest import ApiException

class TestFinalResult(unittest.TestCase):
    """FinalResult unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test FinalResult
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = compute_api_client.models.final_result.FinalResult()  # noqa: E501
        if include_optional :
            return FinalResult(
                created_on = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                id = 1.0, 
                final_result = None, 
                run_id = 1.0
            )
        else :
            return FinalResult(
                created_on = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                id = 1.0,
                run_id = 1.0,
        )

    def testFinalResult(self):
        """Test FinalResult"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
