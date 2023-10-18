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


class ProjectPatch(object):
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
        'owner_id': 'int',
        'name': 'str',
        'description': 'str',
        'starred': 'bool'
    }

    attribute_map = {
        'owner_id': 'owner_id',
        'name': 'name',
        'description': 'description',
        'starred': 'starred'
    }

    def __init__(self, owner_id=None, name=None, description=None, starred=None, local_vars_configuration=None):  # noqa: E501
        """ProjectPatch - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._owner_id = None
        self._name = None
        self._description = None
        self._starred = None
        self.discriminator = None

        if owner_id is not None:
            self.owner_id = owner_id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if starred is not None:
            self.starred = starred

    @property
    def owner_id(self):
        """Gets the owner_id of this ProjectPatch.  # noqa: E501


        :return: The owner_id of this ProjectPatch.  # noqa: E501
        :rtype: int
        """
        return self._owner_id

    @owner_id.setter
    def owner_id(self, owner_id):
        """Sets the owner_id of this ProjectPatch.


        :param owner_id: The owner_id of this ProjectPatch.  # noqa: E501
        :type owner_id: int
        """

        self._owner_id = owner_id

    @property
    def name(self):
        """Gets the name of this ProjectPatch.  # noqa: E501


        :return: The name of this ProjectPatch.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ProjectPatch.


        :param name: The name of this ProjectPatch.  # noqa: E501
        :type name: str
        """
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) > 255):
            raise ValueError("Invalid value for `name`, length must be less than or equal to `255`")  # noqa: E501

        self._name = name

    @property
    def description(self):
        """Gets the description of this ProjectPatch.  # noqa: E501


        :return: The description of this ProjectPatch.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ProjectPatch.


        :param description: The description of this ProjectPatch.  # noqa: E501
        :type description: str
        """

        self._description = description

    @property
    def starred(self):
        """Gets the starred of this ProjectPatch.  # noqa: E501


        :return: The starred of this ProjectPatch.  # noqa: E501
        :rtype: bool
        """
        return self._starred

    @starred.setter
    def starred(self, starred):
        """Sets the starred of this ProjectPatch.


        :param starred: The starred of this ProjectPatch.  # noqa: E501
        :type starred: bool
        """

        self._starred = starred

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
        if not isinstance(other, ProjectPatch):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ProjectPatch):
            return True

        return self.to_dict() != other.to_dict()
