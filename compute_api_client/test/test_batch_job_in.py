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

from compute_api_client.models.batch_job_in import BatchJobIn

class TestBatchJobIn(unittest.TestCase):
    """BatchJobIn unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BatchJobIn:
        """Test BatchJobIn
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BatchJobIn`
        """
        model = BatchJobIn()
        if include_optional:
            return BatchJobIn(
                user_id = 56,
                backend_type_id = 56
            )
        else:
            return BatchJobIn(
                user_id = 56,
                backend_type_id = 56,
        )
        """

    def testBatchJobIn(self):
        """Test BatchJobIn"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
