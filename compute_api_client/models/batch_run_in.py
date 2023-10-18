# coding: utf-8

"""
    Quantum Inspire 2

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


class BatchRunIn(object):
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
        'user_id': 'int',
        'runtime_type_id': 'int'
    }

    attribute_map = {
        'user_id': 'user_id',
        'runtime_type_id': 'runtime_type_id'
    }

    def __init__(self, user_id=None, runtime_type_id=None, local_vars_configuration=None):  # noqa: E501
        """BatchRunIn - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._user_id = None
        self._runtime_type_id = None
        self.discriminator = None

        self.user_id = user_id
        self.runtime_type_id = runtime_type_id

    @property
    def user_id(self):
        """Gets the user_id of this BatchRunIn.  # noqa: E501


        :return: The user_id of this BatchRunIn.  # noqa: E501
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this BatchRunIn.


        :param user_id: The user_id of this BatchRunIn.  # noqa: E501
        :type user_id: int
        """
        if self.local_vars_configuration.client_side_validation and user_id is None:  # noqa: E501
            raise ValueError("Invalid value for `user_id`, must not be `None`")  # noqa: E501

        self._user_id = user_id

    @property
    def runtime_type_id(self):
        """Gets the runtime_type_id of this BatchRunIn.  # noqa: E501


        :return: The runtime_type_id of this BatchRunIn.  # noqa: E501
        :rtype: int
        """
        return self._runtime_type_id

    @runtime_type_id.setter
    def runtime_type_id(self, runtime_type_id):
        """Sets the runtime_type_id of this BatchRunIn.


        :param runtime_type_id: The runtime_type_id of this BatchRunIn.  # noqa: E501
        :type runtime_type_id: int
        """
        if self.local_vars_configuration.client_side_validation and runtime_type_id is None:  # noqa: E501
            raise ValueError("Invalid value for `runtime_type_id`, must not be `None`")  # noqa: E501

        self._runtime_type_id = runtime_type_id

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
        if not isinstance(other, BatchRunIn):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BatchRunIn):
            return True

        return self.to_dict() != other.to_dict()
