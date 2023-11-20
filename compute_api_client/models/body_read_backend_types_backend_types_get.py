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


class BodyReadBackendTypesBackendTypesGet(object):
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
        'features': 'list[str]',
        'default_compiler_config': 'object',
        'native_gateset': 'object'
    }

    attribute_map = {
        'features': 'features',
        'default_compiler_config': 'default_compiler_config',
        'native_gateset': 'native_gateset'
    }

    def __init__(self, features=None, default_compiler_config=None, native_gateset=None, local_vars_configuration=None):  # noqa: E501
        """BodyReadBackendTypesBackendTypesGet - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._features = None
        self._default_compiler_config = None
        self._native_gateset = None
        self.discriminator = None

        if features is not None:
            self.features = features
        if default_compiler_config is not None:
            self.default_compiler_config = default_compiler_config
        if native_gateset is not None:
            self.native_gateset = native_gateset

    @property
    def features(self):
        """Gets the features of this BodyReadBackendTypesBackendTypesGet.  # noqa: E501


        :return: The features of this BodyReadBackendTypesBackendTypesGet.  # noqa: E501
        :rtype: list[str]
        """
        return self._features

    @features.setter
    def features(self, features):
        """Sets the features of this BodyReadBackendTypesBackendTypesGet.


        :param features: The features of this BodyReadBackendTypesBackendTypesGet.  # noqa: E501
        :type features: list[str]
        """

        self._features = features

    @property
    def default_compiler_config(self):
        """Gets the default_compiler_config of this BodyReadBackendTypesBackendTypesGet.  # noqa: E501


        :return: The default_compiler_config of this BodyReadBackendTypesBackendTypesGet.  # noqa: E501
        :rtype: object
        """
        return self._default_compiler_config

    @default_compiler_config.setter
    def default_compiler_config(self, default_compiler_config):
        """Sets the default_compiler_config of this BodyReadBackendTypesBackendTypesGet.


        :param default_compiler_config: The default_compiler_config of this BodyReadBackendTypesBackendTypesGet.  # noqa: E501
        :type default_compiler_config: object
        """

        self._default_compiler_config = default_compiler_config

    @property
    def native_gateset(self):
        """Gets the native_gateset of this BodyReadBackendTypesBackendTypesGet.  # noqa: E501


        :return: The native_gateset of this BodyReadBackendTypesBackendTypesGet.  # noqa: E501
        :rtype: object
        """
        return self._native_gateset

    @native_gateset.setter
    def native_gateset(self, native_gateset):
        """Sets the native_gateset of this BodyReadBackendTypesBackendTypesGet.


        :param native_gateset: The native_gateset of this BodyReadBackendTypesBackendTypesGet.  # noqa: E501
        :type native_gateset: object
        """

        self._native_gateset = native_gateset

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
        if not isinstance(other, BodyReadBackendTypesBackendTypesGet):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BodyReadBackendTypesBackendTypesGet):
            return True

        return self.to_dict() != other.to_dict()