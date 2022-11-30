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


class Transaction(object):
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
        'domain': 'Domain',
        'run': 'int',
        'change': 'int',
        'timestamp': 'datetime',
        'team_id': 'int',
        'user_id': 'int'
    }

    attribute_map = {
        'id': 'id',
        'domain': 'domain',
        'run': 'run',
        'change': 'change',
        'timestamp': 'timestamp',
        'team_id': 'team_id',
        'user_id': 'user_id'
    }

    def __init__(self, id=None, domain=None, run=None, change=None, timestamp=None, team_id=None, user_id=None, local_vars_configuration=None):  # noqa: E501
        """Transaction - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._domain = None
        self._run = None
        self._change = None
        self._timestamp = None
        self._team_id = None
        self._user_id = None
        self.discriminator = None

        self.id = id
        self.domain = domain
        self.run = run
        self.change = change
        self.timestamp = timestamp
        self.team_id = team_id
        self.user_id = user_id

    @property
    def id(self):
        """Gets the id of this Transaction.  # noqa: E501


        :return: The id of this Transaction.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Transaction.


        :param id: The id of this Transaction.  # noqa: E501
        :type id: int
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                id is not None and id > 2147483647):  # noqa: E501
            raise ValueError("Invalid value for `id`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                id is not None and id < 1):  # noqa: E501
            raise ValueError("Invalid value for `id`, must be a value greater than or equal to `1`")  # noqa: E501

        self._id = id

    @property
    def domain(self):
        """Gets the domain of this Transaction.  # noqa: E501

        COMPUTE: compute<br/>NETWORKING: networking<br/>SIMULATE: simulate  # noqa: E501

        :return: The domain of this Transaction.  # noqa: E501
        :rtype: Domain
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this Transaction.

        COMPUTE: compute<br/>NETWORKING: networking<br/>SIMULATE: simulate  # noqa: E501

        :param domain: The domain of this Transaction.  # noqa: E501
        :type domain: Domain
        """
        if (self.local_vars_configuration.client_side_validation and
                domain is not None and len(domain) > 10):
            raise ValueError("Invalid value for `domain`, length must be less than or equal to `10`")  # noqa: E501

        self._domain = domain

    @property
    def run(self):
        """Gets the run of this Transaction.  # noqa: E501


        :return: The run of this Transaction.  # noqa: E501
        :rtype: int
        """
        return self._run

    @run.setter
    def run(self, run):
        """Sets the run of this Transaction.


        :param run: The run of this Transaction.  # noqa: E501
        :type run: int
        """
        if (self.local_vars_configuration.client_side_validation and
                run is not None and run > 2147483647):  # noqa: E501
            raise ValueError("Invalid value for `run`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                run is not None and run < -2147483648):  # noqa: E501
            raise ValueError("Invalid value for `run`, must be a value greater than or equal to `-2147483648`")  # noqa: E501

        self._run = run

    @property
    def change(self):
        """Gets the change of this Transaction.  # noqa: E501


        :return: The change of this Transaction.  # noqa: E501
        :rtype: int
        """
        return self._change

    @change.setter
    def change(self, change):
        """Sets the change of this Transaction.


        :param change: The change of this Transaction.  # noqa: E501
        :type change: int
        """
        if self.local_vars_configuration.client_side_validation and change is None:  # noqa: E501
            raise ValueError("Invalid value for `change`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                change is not None and change > 32767):  # noqa: E501
            raise ValueError("Invalid value for `change`, must be a value less than or equal to `32767`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                change is not None and change < -32768):  # noqa: E501
            raise ValueError("Invalid value for `change`, must be a value greater than or equal to `-32768`")  # noqa: E501

        self._change = change

    @property
    def timestamp(self):
        """Gets the timestamp of this Transaction.  # noqa: E501


        :return: The timestamp of this Transaction.  # noqa: E501
        :rtype: datetime
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this Transaction.


        :param timestamp: The timestamp of this Transaction.  # noqa: E501
        :type timestamp: datetime
        """
        if self.local_vars_configuration.client_side_validation and timestamp is None:  # noqa: E501
            raise ValueError("Invalid value for `timestamp`, must not be `None`")  # noqa: E501

        self._timestamp = timestamp

    @property
    def team_id(self):
        """Gets the team_id of this Transaction.  # noqa: E501


        :return: The team_id of this Transaction.  # noqa: E501
        :rtype: int
        """
        return self._team_id

    @team_id.setter
    def team_id(self, team_id):
        """Sets the team_id of this Transaction.


        :param team_id: The team_id of this Transaction.  # noqa: E501
        :type team_id: int
        """
        if self.local_vars_configuration.client_side_validation and team_id is None:  # noqa: E501
            raise ValueError("Invalid value for `team_id`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                team_id is not None and team_id > 2147483647):  # noqa: E501
            raise ValueError("Invalid value for `team_id`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                team_id is not None and team_id < 1):  # noqa: E501
            raise ValueError("Invalid value for `team_id`, must be a value greater than or equal to `1`")  # noqa: E501

        self._team_id = team_id

    @property
    def user_id(self):
        """Gets the user_id of this Transaction.  # noqa: E501


        :return: The user_id of this Transaction.  # noqa: E501
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this Transaction.


        :param user_id: The user_id of this Transaction.  # noqa: E501
        :type user_id: int
        """
        if (self.local_vars_configuration.client_side_validation and
                user_id is not None and user_id > 2147483647):  # noqa: E501
            raise ValueError("Invalid value for `user_id`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                user_id is not None and user_id < 1):  # noqa: E501
            raise ValueError("Invalid value for `user_id`, must be a value greater than or equal to `1`")  # noqa: E501

        self._user_id = user_id

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
        if not isinstance(other, Transaction):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Transaction):
            return True

        return self.to_dict() != other.to_dict()
