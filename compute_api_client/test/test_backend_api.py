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
from compute_api_client.api.backend_api import BackendApi  # noqa: E501
from compute_api_client.rest import ApiException


class TestBackendApi(unittest.TestCase):
    """BackendApi unit test stubs"""

    def setUp(self):
        self.api = compute_api_client.api.backend_api.BackendApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_backend_backends_post(self):
        """Test case for create_backend_backends_post

        Create backend  # noqa: E501
        """
        pass

    def test_read_backend_backends_id_get(self):
        """Test case for read_backend_backends_id_get

        Retrieve backend  # noqa: E501
        """
        pass

    def test_read_backends_backends_get(self):
        """Test case for read_backends_backends_get

        List backends  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
