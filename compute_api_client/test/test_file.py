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

from compute_api_client.models.file import File

class TestFile(unittest.TestCase):
    """File unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> File:
        """Test File
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `File`
        """
        model = File()
        if include_optional:
            return File(
                id = 56,
                commit_id = 56,
                content = '',
                language_id = 56,
                compile_stage = 'none',
                compile_properties = compute_api_client.models.compile_properties.Compile Properties(),
                generated = True
            )
        else:
            return File(
                id = 56,
                commit_id = 56,
                content = '',
                language_id = 56,
                compile_stage = 'none',
                compile_properties = compute_api_client.models.compile_properties.Compile Properties(),
                generated = True,
        )
        """

    def testFile(self):
        """Test File"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
