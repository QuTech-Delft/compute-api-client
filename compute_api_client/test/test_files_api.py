# coding: utf-8

"""
    Compute Job Manager

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.1.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import compute_api_client
from compute_api_client.api.files_api import FilesApi  # noqa: E501
from compute_api_client.rest import ApiException


class TestFilesApi(unittest.TestCase):
    """FilesApi unit test stubs"""

    def setUp(self):
        self.api = compute_api_client.api.files_api.FilesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_file_files_post(self):
        """Test case for create_file_files_post

        Create file  # noqa: E501
        """
        pass

    def test_delete_file_files_id_delete(self):
        """Test case for delete_file_files_id_delete

        Destroy file  # noqa: E501
        """
        pass

    def test_read_file_files_id_get(self):
        """Test case for read_file_files_id_get

        Retrieve file  # noqa: E501
        """
        pass

    def test_read_files_files_get(self):
        """Test case for read_files_files_get

        List files  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
