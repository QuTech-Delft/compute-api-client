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
from compute_api_client.models.file_in import FileIn  # noqa: E501
from compute_api_client.rest import ApiException

class TestFileIn(unittest.TestCase):
    """FileIn unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test FileIn
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = compute_api_client.models.file_in.FileIn()  # noqa: E501
        if include_optional :
            return FileIn(
                commit_id = 56, 
                content = '', 
                language_id = 56, 
                compile_stage = 'none', 
                compile_properties = compute_api_client.models.compile_properties.Compile Properties(), 
                generated = True
            )
        else :
            return FileIn(
                commit_id = 56,
                content = '',
                language_id = 56,
                compile_stage = 'none',
                compile_properties = compute_api_client.models.compile_properties.Compile Properties(),
        )

    def testFileIn(self):
        """Test FileIn"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
