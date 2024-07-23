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

from compute_api_client.models.page_language import PageLanguage

class TestPageLanguage(unittest.TestCase):
    """PageLanguage unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PageLanguage:
        """Test PageLanguage
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PageLanguage`
        """
        model = PageLanguage()
        if include_optional:
            return PageLanguage(
                items = [
                    compute_api_client.models.language.Language(
                        id = 56, 
                        name = '', 
                        version = '', )
                    ],
                total = 0.0,
                page = 1.0,
                size = 1.0,
                pages = 0.0
            )
        else:
            return PageLanguage(
                items = [
                    compute_api_client.models.language.Language(
                        id = 56, 
                        name = '', 
                        version = '', )
                    ],
                total = 0.0,
                page = 1.0,
                size = 1.0,
        )
        """

    def testPageLanguage(self):
        """Test PageLanguage"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()