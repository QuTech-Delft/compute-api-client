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

from compute_api_client.models.project_in import ProjectIn

class TestProjectIn(unittest.TestCase):
    """ProjectIn unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ProjectIn:
        """Test ProjectIn
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ProjectIn`
        """
        model = ProjectIn()
        if include_optional:
            return ProjectIn(
                owner_id = 56,
                name = '',
                description = '',
                starred = True
            )
        else:
            return ProjectIn(
                owner_id = 56,
                name = '',
                description = '',
        )
        """

    def testProjectIn(self):
        """Test ProjectIn"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
