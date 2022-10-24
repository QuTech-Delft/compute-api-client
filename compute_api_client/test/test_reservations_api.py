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
from compute_api_client.api.reservations_api import ReservationsApi  # noqa: E501
from compute_api_client.rest import ApiException


class TestReservationsApi(unittest.TestCase):
    """ReservationsApi unit test stubs"""

    def setUp(self):
        self.api = compute_api_client.api.reservations_api.ReservationsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_reservation_reservations_post(self):
        """Test case for create_reservation_reservations_post

        Create reservation  # noqa: E501
        """
        pass

    def test_read_reservation_reservations_id_get(self):
        """Test case for read_reservation_reservations_id_get

        Retrieve reservation  # noqa: E501
        """
        pass

    def test_read_reservations_reservations_get(self):
        """Test case for read_reservations_reservations_get

        List reservations  # noqa: E501
        """
        pass

    def test_terminate_reservation_reservations_id_terminate_patch(self):
        """Test case for terminate_reservation_reservations_id_terminate_patch

        Terminate reservation  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
