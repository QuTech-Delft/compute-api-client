# coding: utf-8

"""
    Quantum Inspire 2

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from compute_api_client.api.auth_config_api import AuthConfigApi


class TestAuthConfigApi(unittest.TestCase):
    """AuthConfigApi unit test stubs"""

    def setUp(self) -> None:
        self.api = AuthConfigApi()

    def tearDown(self) -> None:
        pass

    def test_auth_config_auth_config_get(self) -> None:
        """Test case for auth_config_auth_config_get

        Get suggested authentication configuration
        """
        pass


if __name__ == '__main__':
    unittest.main()