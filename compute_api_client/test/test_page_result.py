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

from compute_api_client.models.page_result import PageResult

class TestPageResult(unittest.TestCase):
    """PageResult unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PageResult:
        """Test PageResult
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PageResult`
        """
        model = PageResult()
        if include_optional:
            return PageResult(
                items = [
                    compute_api_client.models.result.Result(
                        id = 56, 
                        created_on = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        job_id = 56, 
                        metadata_id = 56, 
                        number_of_qubits = -32768.0, 
                        execution_time_in_seconds = 1.337, 
                        shots_requested = 56, 
                        shots_done = 56, 
                        results = compute_api_client.models.results.results(), )
                    ],
                total = 0.0,
                page = 1.0,
                size = 1.0,
                pages = 0.0
            )
        else:
            return PageResult(
                items = [
                    compute_api_client.models.result.Result(
                        id = 56, 
                        created_on = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        job_id = 56, 
                        metadata_id = 56, 
                        number_of_qubits = -32768.0, 
                        execution_time_in_seconds = 1.337, 
                        shots_requested = 56, 
                        shots_done = 56, 
                        results = compute_api_client.models.results.results(), )
                    ],
                total = 0.0,
                page = 1.0,
                size = 1.0,
        )
        """

    def testPageResult(self):
        """Test PageResult"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
