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

from compute_api_client.models.member import Member

class TestMember(unittest.TestCase):
    """Member unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Member:
        """Test Member
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Member`
        """
        model = Member()
        if include_optional:
            return Member(
                id = 56,
                team_id = 56,
                user_id = 56,
                role = 'member',
                is_active = True
            )
        else:
            return Member(
                id = 56,
                team_id = 56,
                user_id = 56,
                role = 'member',
                is_active = True,
        )
        """

    def testMember(self):
        """Test Member"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
