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


class Commit(object):
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
        'id': 'int',
        'created_on': 'datetime',
        'hash': 'str',
        'description': 'str',
        'algorithm_id': 'int'
    }

    attribute_map = {
        'id': 'id',
        'created_on': 'created_on',
        'hash': 'hash',
        'description': 'description',
        'algorithm_id': 'algorithm_id'
    }

    def __init__(self, id=None, created_on=None, hash=None, description=None, algorithm_id=None, local_vars_configuration=None):  # noqa: E501
        """Commit - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._created_on = None
        self._hash = None
        self._description = None
        self._algorithm_id = None
        self.discriminator = None

        self.id = id
        self.created_on = created_on
        self.hash = hash
        self.description = description
        self.algorithm_id = algorithm_id

    @property
    def id(self):
        """Gets the id of this Commit.  # noqa: E501


        :return: The id of this Commit.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Commit.


        :param id: The id of this Commit.  # noqa: E501
        :type id: int
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def created_on(self):
        """Gets the created_on of this Commit.  # noqa: E501


        :return: The created_on of this Commit.  # noqa: E501
        :rtype: datetime
        """
        return self._created_on

    @created_on.setter
    def created_on(self, created_on):
        """Sets the created_on of this Commit.


        :param created_on: The created_on of this Commit.  # noqa: E501
        :type created_on: datetime
        """
        if self.local_vars_configuration.client_side_validation and created_on is None:  # noqa: E501
            raise ValueError("Invalid value for `created_on`, must not be `None`")  # noqa: E501

        self._created_on = created_on

    @property
    def hash(self):
        """Gets the hash of this Commit.  # noqa: E501


        :return: The hash of this Commit.  # noqa: E501
        :rtype: str
        """
        return self._hash

    @hash.setter
    def hash(self, hash):
        """Sets the hash of this Commit.


        :param hash: The hash of this Commit.  # noqa: E501
        :type hash: str
        """
        if self.local_vars_configuration.client_side_validation and hash is None:  # noqa: E501
            raise ValueError("Invalid value for `hash`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                hash is not None and len(hash) > 32):
            raise ValueError("Invalid value for `hash`, length must be less than or equal to `32`")  # noqa: E501

        self._hash = hash

    @property
    def description(self):
        """Gets the description of this Commit.  # noqa: E501


        :return: The description of this Commit.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Commit.


        :param description: The description of this Commit.  # noqa: E501
        :type description: str
        """
        if self.local_vars_configuration.client_side_validation and description is None:  # noqa: E501
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def algorithm_id(self):
        """Gets the algorithm_id of this Commit.  # noqa: E501


        :return: The algorithm_id of this Commit.  # noqa: E501
        :rtype: int
        """
        return self._algorithm_id

    @algorithm_id.setter
    def algorithm_id(self, algorithm_id):
        """Sets the algorithm_id of this Commit.


        :param algorithm_id: The algorithm_id of this Commit.  # noqa: E501
        :type algorithm_id: int
        """
        if self.local_vars_configuration.client_side_validation and algorithm_id is None:  # noqa: E501
            raise ValueError("Invalid value for `algorithm_id`, must not be `None`")  # noqa: E501

        self._algorithm_id = algorithm_id

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
        if not isinstance(other, Commit):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Commit):
            return True

        return self.to_dict() != other.to_dict()
