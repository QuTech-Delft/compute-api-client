# coding: utf-8

"""
    Quantum Inspire 2

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from compute_api_client.api.languages_api import LanguagesApi


class TestLanguagesApi(unittest.TestCase):
    """LanguagesApi unit test stubs"""

    def setUp(self) -> None:
        self.api = LanguagesApi()

    def tearDown(self) -> None:
        pass

    def test_read_language_languages_id_get(self) -> None:
        """Test case for read_language_languages_id_get

        Retrieve language
        """
        pass

    def test_read_languages_languages_get(self) -> None:
        """Test case for read_languages_languages_get

        List languages
        """
        pass


if __name__ == '__main__':
    unittest.main()
