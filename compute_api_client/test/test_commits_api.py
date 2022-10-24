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
from compute_api_client.api.commits_api import CommitsApi  # noqa: E501
from compute_api_client.rest import ApiException


class TestCommitsApi(unittest.TestCase):
    """CommitsApi unit test stubs"""

    def setUp(self):
        self.api = compute_api_client.api.commits_api.CommitsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_commit_commits_post(self):
        """Test case for create_commit_commits_post

        Create commit  # noqa: E501
        """
        pass

    def test_delete_commit_commits_id_delete(self):
        """Test case for delete_commit_commits_id_delete

        Destroy commit  # noqa: E501
        """
        pass

    def test_read_commit_commits_id_get(self):
        """Test case for read_commit_commits_id_get

        Retrieve commit  # noqa: E501
        """
        pass

    def test_read_commits_commits_get(self):
        """Test case for read_commits_commits_get

        List commits  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
