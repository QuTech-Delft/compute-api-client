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
from compute_api_client.models.runtime_with_authentication import RuntimeWithAuthentication  # noqa: E501
from compute_api_client.rest import ApiException

class TestRuntimeWithAuthentication(unittest.TestCase):
    """RuntimeWithAuthentication unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test RuntimeWithAuthentication
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = compute_api_client.models.runtime_with_authentication.RuntimeWithAuthentication()  # noqa: E501
        if include_optional :
            return RuntimeWithAuthentication(
                id = 1.0, 
                name = '', 
                location = '', 
                status = None, 
                last_heartbeat = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                authentication_hash = '', 
                runtime_type_id = 1.0
            )
        else :
            return RuntimeWithAuthentication(
                id = 1.0,
                name = '',
                location = '',
                status = None,
                last_heartbeat = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                authentication_hash = '',
                runtime_type_id = 1.0,
        )

    def testRuntimeWithAuthentication(self):
        """Test RuntimeWithAuthentication"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
