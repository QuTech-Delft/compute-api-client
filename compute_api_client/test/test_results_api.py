# coding: utf-8

"""
    Quantum Inspire 2

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.1.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import compute_api_client
from compute_api_client.api.results_api import ResultsApi  # noqa: E501
from compute_api_client.rest import ApiException


class TestResultsApi(unittest.TestCase):
    """ResultsApi unit test stubs"""

    def setUp(self):
        self.api = compute_api_client.api.results_api.ResultsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_result_results_post(self):
        """Test case for create_result_results_post

        Create result  # noqa: E501
        """
        pass

    def test_read_result_results_id_get(self):
        """Test case for read_result_results_id_get

        Retrieve result  # noqa: E501
        """
        pass

    def test_read_results_by_job_id_results_job_job_id_get(self):
        """Test case for read_results_by_job_id_results_job_job_id_get

        Retrieve result  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
