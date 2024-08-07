# coding: utf-8

"""
    Quantum Inspire 2

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from compute_api_client.models.page_team import PageTeam

class TestPageTeam(unittest.TestCase):
    """PageTeam unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PageTeam:
        """Test PageTeam
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PageTeam`
        """
        model = PageTeam()
        if include_optional:
            return PageTeam(
                items = [
                    compute_api_client.models.team.Team(
                        id = 56, 
                        name = '', 
                        slug = '', 
                        individual_user = True, )
                    ],
                total = 0.0,
                page = 1.0,
                size = 1.0,
                pages = 0.0
            )
        else:
            return PageTeam(
                items = [
                    compute_api_client.models.team.Team(
                        id = 56, 
                        name = '', 
                        slug = '', 
                        individual_user = True, )
                    ],
                total = 0.0,
                page = 1.0,
                size = 1.0,
        )
        """

    def testPageTeam(self):
        """Test PageTeam"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
