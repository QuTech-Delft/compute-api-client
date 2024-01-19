# coding: utf-8

"""
    Quantum Inspire 2

     **Sorting and Pagination of list endpoints**  The api provides sorting and pagination for list endpoints. The following parameters can be passed as query parameters to get sorted and paginated list.  - `latest`     - **Type**: Boolean.     - **Description**: Get the most recently created object. Defaults to False. - `sort_by`     - **Type**: String:     - **Description**: The field / column name to sort on. To reverse sort provide the field with a \"-\" sign. E.g. \"created_on\" for ascending order while \"-created_on\" in descending order. Defaults to \"id\". - `page_number`     - **Type**: Positive Integer     - **Description**: The page number for pagination. Defaults to 1. - `items_per_page`     - **Type**: Positive Integer.     - **Description**: The number of items per page for pagination. Defaults to 50. 

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, ClassVar, Dict, List
from pydantic import BaseModel, StrictBool, StrictInt
from pydantic import Field
from typing_extensions import Annotated
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class User(BaseModel):
    """
    User
    """ # noqa: E501
    id: StrictInt
    full_name: Annotated[str, Field(strict=True, max_length=64)]
    email: Annotated[str, Field(strict=True, max_length=256)]
    is_superuser: StrictBool
    is_staff: StrictBool
    is_active: StrictBool
    is_confirmed: StrictBool
    __properties: ClassVar[List[str]] = ["id", "full_name", "email", "is_superuser", "is_staff", "is_active", "is_confirmed"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of User from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
            },
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of User from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "full_name": obj.get("full_name"),
            "email": obj.get("email"),
            "is_superuser": obj.get("is_superuser"),
            "is_staff": obj.get("is_staff"),
            "is_active": obj.get("is_active"),
            "is_confirmed": obj.get("is_confirmed")
        })
        return _obj


