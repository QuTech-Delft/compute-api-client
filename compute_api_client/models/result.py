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

from datetime import datetime
from typing import Any, ClassVar, Dict, List, Optional, Union
from pydantic import BaseModel, StrictFloat, StrictInt
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class Result(BaseModel):
    """
    Result
    """ # noqa: E501
    id: StrictInt
    created_on: datetime
    job_id: StrictInt
    metadata_id: StrictInt
    execution_time_in_seconds: Union[StrictFloat, StrictInt]
    shots_requested: Optional[StrictInt]
    shots_done: Optional[StrictInt]
    results: Optional[Union[str, Any]]
    __properties: ClassVar[List[str]] = ["id", "created_on", "job_id", "metadata_id", "execution_time_in_seconds", "shots_requested", "shots_done", "results"]

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
        """Create an instance of Result from a JSON string"""
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
        # set to None if shots_requested (nullable) is None
        # and model_fields_set contains the field
        if self.shots_requested is None and "shots_requested" in self.model_fields_set:
            _dict['shots_requested'] = None

        # set to None if shots_done (nullable) is None
        # and model_fields_set contains the field
        if self.shots_done is None and "shots_done" in self.model_fields_set:
            _dict['shots_done'] = None

        # set to None if results (nullable) is None
        # and model_fields_set contains the field
        if self.results is None and "results" in self.model_fields_set:
            _dict['results'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of Result from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "created_on": obj.get("created_on"),
            "job_id": obj.get("job_id"),
            "metadata_id": obj.get("metadata_id"),
            "execution_time_in_seconds": obj.get("execution_time_in_seconds"),
            "shots_requested": obj.get("shots_requested"),
            "shots_done": obj.get("shots_done"),
            "results": obj.get("results")
        })
        return _obj


