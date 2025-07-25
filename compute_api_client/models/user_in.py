# coding: utf-8

"""
    Quantum Inspire 2

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class UserIn(BaseModel):
    """
    UserIn
    """ # noqa: E501
    full_name: Annotated[str, Field(strict=True, max_length=64)] = Field(description="The full name of the user")
    email: Annotated[str, Field(strict=True, max_length=256)] = Field(description="The email id of the user")
    is_superuser: Optional[StrictBool] = Field(default=False, description="If the user is superuser")
    is_staff: Optional[StrictBool] = Field(default=False, description="If the user is staff")
    is_active: Optional[StrictBool] = Field(default=False, description="If the user is active")
    is_confirmed: Optional[StrictBool] = Field(default=False, description="If the user is confirmed")
    oidc_sub: Annotated[str, Field(strict=True, max_length=256)] = Field(description="User identifier from OIDC provider")
    __properties: ClassVar[List[str]] = ["full_name", "email", "is_superuser", "is_staff", "is_active", "is_confirmed", "oidc_sub"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of UserIn from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of UserIn from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "full_name": obj.get("full_name"),
            "email": obj.get("email"),
            "is_superuser": obj.get("is_superuser") if obj.get("is_superuser") is not None else False,
            "is_staff": obj.get("is_staff") if obj.get("is_staff") is not None else False,
            "is_active": obj.get("is_active") if obj.get("is_active") is not None else False,
            "is_confirmed": obj.get("is_confirmed") if obj.get("is_confirmed") is not None else False,
            "oidc_sub": obj.get("oidc_sub")
        })
        return _obj


