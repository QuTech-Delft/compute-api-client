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
from compute_api_client.api.backend_types_api import BackendTypesApi  # noqa: E501
from compute_api_client.rest import ApiException


class TestBackendTypesApi(unittest.TestCase):
    """BackendTypesApi unit test stubs"""

    def setUp(self):
        self.api = compute_api_client.api.backend_types_api.BackendTypesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_read_backend_type_backend_types_id_get(self):
        """Test case for read_backend_type_backend_types_id_get

        Retrieve backend type  # noqa: E501
        """
        pass

    def test_read_backend_types_backend_types_get(self):
        """Test case for read_backend_types_backend_types_get

        List backend types  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
