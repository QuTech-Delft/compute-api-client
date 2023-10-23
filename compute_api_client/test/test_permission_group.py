# coding: utf-8

"""
    Quantum Inspire 2

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.1.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import compute_api_client
from compute_api_client.models.permission_group import PermissionGroup  # noqa: E501
from compute_api_client.rest import ApiException

class TestPermissionGroup(unittest.TestCase):
    """PermissionGroup unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PermissionGroup
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = compute_api_client.models.permission_group.PermissionGroup()  # noqa: E501
        if include_optional :
            return PermissionGroup(
                id = 56, 
                name = ''
            )
        else :
            return PermissionGroup(
                id = 56,
                name = '',
        )

    def testPermissionGroup(self):
        """Test PermissionGroup"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
