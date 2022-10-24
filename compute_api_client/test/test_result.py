# coding: utf-8

"""
    Compute Job Manager

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.1.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import compute_api_client
from compute_api_client.models.result import Result  # noqa: E501
from compute_api_client.rest import ApiException

class TestResult(unittest.TestCase):
    """Result unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Result
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = compute_api_client.models.result.Result()  # noqa: E501
        if include_optional :
            return Result(
                run_id = 56, 
                metadata_id = 56, 
                created_on = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                number_of_qubits = 56, 
                execution_time_in_seconds = 1.337, 
                raw_text = '', 
                raw_data = compute_api_client.models.raw_data.Raw Data(), 
                histogram = {
                    'key' : 1.337
                    }, 
                measurement_mask = compute_api_client.models.measurement_mask.Measurement Mask(), 
                quantum_states = compute_api_client.models.quantum_states.Quantum States(), 
                measurement_register = compute_api_client.models.measurement_register.Measurement Register(), 
                id = 56
            )
        else :
            return Result(
                run_id = 56,
                metadata_id = 56,
                created_on = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                number_of_qubits = 56,
                execution_time_in_seconds = 1.337,
                raw_text = '',
                raw_data = compute_api_client.models.raw_data.Raw Data(),
                histogram = {
                    'key' : 1.337
                    },
                measurement_mask = compute_api_client.models.measurement_mask.Measurement Mask(),
                quantum_states = compute_api_client.models.quantum_states.Quantum States(),
                measurement_register = compute_api_client.models.measurement_register.Measurement Register(),
                id = 56,
        )

    def testResult(self):
        """Test Result"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
