# coding: utf-8

"""
    Quantum Inspire 2

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from compute_api_client.api.backend_types_api import BackendTypesApi


class TestBackendTypesApi(unittest.TestCase):
    """BackendTypesApi unit test stubs"""

    def setUp(self) -> None:
        self.api = BackendTypesApi()

    def tearDown(self) -> None:
        pass

    def test_read_backend_type_backend_types_id_get(self) -> None:
        """Test case for read_backend_type_backend_types_id_get

        Retrieve backend type
        """
        pass

    def test_read_backend_types_backend_types_get(self) -> None:
        """Test case for read_backend_types_backend_types_get

        List backend types
        """
        pass


if __name__ == '__main__':
    unittest.main()
