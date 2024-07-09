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


from typing import Any, ClassVar, Dict, List, Optional, Union
from pydantic import BaseModel, StrictFloat, StrictInt
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class ResultIn(BaseModel):
    """
    ResultIn
    """ # noqa: E501
    job_id: StrictInt
    metadata_id: Optional[StrictInt] = None
    execution_time_in_seconds: Union[StrictFloat, StrictInt]
    shots_requested: Optional[StrictInt] = None
    shots_done: Optional[StrictInt] = None
    results: Optional[Union[str, Any]] = None
    __properties: ClassVar[List[str]] = ["job_id", "metadata_id", "execution_time_in_seconds", "shots_requested", "shots_done", "results"]

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
        """Create an instance of ResultIn from a JSON string"""
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
        # set to None if metadata_id (nullable) is None
        # and model_fields_set contains the field
        if self.metadata_id is None and "metadata_id" in self.model_fields_set:
            _dict['metadata_id'] = None

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
        """Create an instance of ResultIn from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "job_id": obj.get("job_id"),
            "metadata_id": obj.get("metadata_id"),
            "execution_time_in_seconds": obj.get("execution_time_in_seconds"),
            "shots_requested": obj.get("shots_requested"),
            "shots_done": obj.get("shots_done"),
            "results": obj.get("results")
        })
        return _obj


