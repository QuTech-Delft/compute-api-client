# coding: utf-8

"""
    Quantum Inspire 2

     **Sorting and Pagination of list endpoints**  The api provides sorting and pagination for list endpoints. The following parameters can be passed as query parameters to get sorted and paginated list.  - `latest`     - **Type**: Boolean.     - **Description**: Get the most recently created object. Defaults to False. - `sort_by`     - **Type**: String:     - **Description**: The field / column name to sort on. To reverse sort provide the field with a \"-\" sign. E.g. \"created_on\" for ascending order while \"-created_on\" in descending order. Defaults to \"id\". - `page_number`     - **Type**: Positive Integer     - **Description**: The page number for pagination. Defaults to 1. - `items_per_page`     - **Type**: Positive Integer.     - **Description**: The number of items per page for pagination. Defaults to 50. 

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
import pprint
import re  # noqa: F401
from enum import Enum



try:
    from typing import Self
except ImportError:
    from typing_extensions import Self


class ShareType(str, Enum):
    """
    ShareType
    """

    """
    allowed enum values
    """
    PRIVATE = 'private'
    LINK_ONLY = 'link_only'
    TEAM = 'team'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of ShareType from a JSON string"""
        return cls(json.loads(json_str))


