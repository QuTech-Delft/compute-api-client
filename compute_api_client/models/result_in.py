# coding: utf-8

"""
    Compute Job Manager

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.1.0
    Generated by: https://openapi-generator.tech
"""


try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from compute_api_client.configuration import Configuration


class ResultIn(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'number_of_qubits': 'int',
        'execution_time_in_seconds': 'float',
        'raw_text': 'str',
        'raw_data': 'object',
        'histogram': 'object',
        'measurement_mask': 'object',
        'quantum_states': 'object',
        'measurement_register': 'object',
        'run_id': 'int'
    }

    attribute_map = {
        'number_of_qubits': 'number_of_qubits',
        'execution_time_in_seconds': 'execution_time_in_seconds',
        'raw_text': 'raw_text',
        'raw_data': 'raw_data',
        'histogram': 'histogram',
        'measurement_mask': 'measurement_mask',
        'quantum_states': 'quantum_states',
        'measurement_register': 'measurement_register',
        'run_id': 'run_id'
    }

    def __init__(self, number_of_qubits=None, execution_time_in_seconds=None, raw_text=None, raw_data=None, histogram=None, measurement_mask=None, quantum_states=None, measurement_register=None, run_id=None, local_vars_configuration=None):  # noqa: E501
        """ResultIn - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._number_of_qubits = None
        self._execution_time_in_seconds = None
        self._raw_text = None
        self._raw_data = None
        self._histogram = None
        self._measurement_mask = None
        self._quantum_states = None
        self._measurement_register = None
        self._run_id = None
        self.discriminator = None

        self.number_of_qubits = number_of_qubits
        self.execution_time_in_seconds = execution_time_in_seconds
        self.raw_text = raw_text
        self.raw_data = raw_data
        self.histogram = histogram
        self.measurement_mask = measurement_mask
        self.quantum_states = quantum_states
        self.measurement_register = measurement_register
        self.run_id = run_id

    @property
    def number_of_qubits(self):
        """Gets the number_of_qubits of this ResultIn.  # noqa: E501


        :return: The number_of_qubits of this ResultIn.  # noqa: E501
        :rtype: int
        """
        return self._number_of_qubits

    @number_of_qubits.setter
    def number_of_qubits(self, number_of_qubits):
        """Sets the number_of_qubits of this ResultIn.


        :param number_of_qubits: The number_of_qubits of this ResultIn.  # noqa: E501
        :type number_of_qubits: int
        """
        if self.local_vars_configuration.client_side_validation and number_of_qubits is None:  # noqa: E501
            raise ValueError("Invalid value for `number_of_qubits`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                number_of_qubits is not None and number_of_qubits > 32767):  # noqa: E501
            raise ValueError("Invalid value for `number_of_qubits`, must be a value less than or equal to `32767`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                number_of_qubits is not None and number_of_qubits < -32768):  # noqa: E501
            raise ValueError("Invalid value for `number_of_qubits`, must be a value greater than or equal to `-32768`")  # noqa: E501

        self._number_of_qubits = number_of_qubits

    @property
    def execution_time_in_seconds(self):
        """Gets the execution_time_in_seconds of this ResultIn.  # noqa: E501


        :return: The execution_time_in_seconds of this ResultIn.  # noqa: E501
        :rtype: float
        """
        return self._execution_time_in_seconds

    @execution_time_in_seconds.setter
    def execution_time_in_seconds(self, execution_time_in_seconds):
        """Sets the execution_time_in_seconds of this ResultIn.


        :param execution_time_in_seconds: The execution_time_in_seconds of this ResultIn.  # noqa: E501
        :type execution_time_in_seconds: float
        """
        if self.local_vars_configuration.client_side_validation and execution_time_in_seconds is None:  # noqa: E501
            raise ValueError("Invalid value for `execution_time_in_seconds`, must not be `None`")  # noqa: E501

        self._execution_time_in_seconds = execution_time_in_seconds

    @property
    def raw_text(self):
        """Gets the raw_text of this ResultIn.  # noqa: E501


        :return: The raw_text of this ResultIn.  # noqa: E501
        :rtype: str
        """
        return self._raw_text

    @raw_text.setter
    def raw_text(self, raw_text):
        """Sets the raw_text of this ResultIn.


        :param raw_text: The raw_text of this ResultIn.  # noqa: E501
        :type raw_text: str
        """
        if self.local_vars_configuration.client_side_validation and raw_text is None:  # noqa: E501
            raise ValueError("Invalid value for `raw_text`, must not be `None`")  # noqa: E501

        self._raw_text = raw_text

    @property
    def raw_data(self):
        """Gets the raw_data of this ResultIn.  # noqa: E501


        :return: The raw_data of this ResultIn.  # noqa: E501
        :rtype: object
        """
        return self._raw_data

    @raw_data.setter
    def raw_data(self, raw_data):
        """Sets the raw_data of this ResultIn.


        :param raw_data: The raw_data of this ResultIn.  # noqa: E501
        :type raw_data: object
        """

        self._raw_data = raw_data

    @property
    def histogram(self):
        """Gets the histogram of this ResultIn.  # noqa: E501


        :return: The histogram of this ResultIn.  # noqa: E501
        :rtype: object
        """
        return self._histogram

    @histogram.setter
    def histogram(self, histogram):
        """Sets the histogram of this ResultIn.


        :param histogram: The histogram of this ResultIn.  # noqa: E501
        :type histogram: object
        """

        self._histogram = histogram

    @property
    def measurement_mask(self):
        """Gets the measurement_mask of this ResultIn.  # noqa: E501


        :return: The measurement_mask of this ResultIn.  # noqa: E501
        :rtype: object
        """
        return self._measurement_mask

    @measurement_mask.setter
    def measurement_mask(self, measurement_mask):
        """Sets the measurement_mask of this ResultIn.


        :param measurement_mask: The measurement_mask of this ResultIn.  # noqa: E501
        :type measurement_mask: object
        """

        self._measurement_mask = measurement_mask

    @property
    def quantum_states(self):
        """Gets the quantum_states of this ResultIn.  # noqa: E501


        :return: The quantum_states of this ResultIn.  # noqa: E501
        :rtype: object
        """
        return self._quantum_states

    @quantum_states.setter
    def quantum_states(self, quantum_states):
        """Sets the quantum_states of this ResultIn.


        :param quantum_states: The quantum_states of this ResultIn.  # noqa: E501
        :type quantum_states: object
        """

        self._quantum_states = quantum_states

    @property
    def measurement_register(self):
        """Gets the measurement_register of this ResultIn.  # noqa: E501


        :return: The measurement_register of this ResultIn.  # noqa: E501
        :rtype: object
        """
        return self._measurement_register

    @measurement_register.setter
    def measurement_register(self, measurement_register):
        """Sets the measurement_register of this ResultIn.


        :param measurement_register: The measurement_register of this ResultIn.  # noqa: E501
        :type measurement_register: object
        """

        self._measurement_register = measurement_register

    @property
    def run_id(self):
        """Gets the run_id of this ResultIn.  # noqa: E501


        :return: The run_id of this ResultIn.  # noqa: E501
        :rtype: int
        """
        return self._run_id

    @run_id.setter
    def run_id(self, run_id):
        """Sets the run_id of this ResultIn.


        :param run_id: The run_id of this ResultIn.  # noqa: E501
        :type run_id: int
        """
        if self.local_vars_configuration.client_side_validation and run_id is None:  # noqa: E501
            raise ValueError("Invalid value for `run_id`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                run_id is not None and run_id > 2147483647):  # noqa: E501
            raise ValueError("Invalid value for `run_id`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                run_id is not None and run_id < 1):  # noqa: E501
            raise ValueError("Invalid value for `run_id`, must be a value greater than or equal to `1`")  # noqa: E501

        self._run_id = run_id

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = getfullargspec(x.to_dict).args
                if len(args) == 1:
                    return x.to_dict()
                else:
                    return x.to_dict(serialize)
            else:
                return x

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            attr = self.attribute_map.get(attr, attr) if serialize else attr
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: convert(x),
                    value
                ))
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], convert(item[1])),
                    value.items()
                ))
            else:
                result[attr] = convert(value)

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ResultIn):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ResultIn):
            return True

        return self.to_dict() != other.to_dict()
