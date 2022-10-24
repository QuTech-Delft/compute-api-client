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
from compute_api_client.models.team import Team  # noqa: E501
from compute_api_client.rest import ApiException

class TestTeam(unittest.TestCase):
    """Team unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Team
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = compute_api_client.models.team.Team()  # noqa: E501
        if include_optional :
            return Team(
                name = '', 
                slug = '', 
                permission_group_ids = [
                    56
                    ], 
                permission_ids = [
                    56
                    ], 
                individual_user = True, 
                id = 56
            )
        else :
            return Team(
                name = '',
                slug = '',
                permission_group_ids = [
                    56
                    ],
                permission_ids = [
                    56
                    ],
                individual_user = True,
                id = 56,
        )

    def testTeam(self):
        """Test Team"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
