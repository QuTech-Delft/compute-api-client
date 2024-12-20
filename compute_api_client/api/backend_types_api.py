# coding: utf-8

"""
    Quantum Inspire 2

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import io
import warnings

from pydantic import validate_call, Field, StrictFloat, StrictStr, StrictInt
from typing import Dict, List, Optional, Tuple, Union, Any

try:
    from typing import Annotated
except ImportError:
    from typing_extensions import Annotated

from pydantic import Field
from typing_extensions import Annotated
from pydantic import StrictBool, StrictInt, StrictStr

from typing import Optional

from compute_api_client.models.backend_status import BackendStatus
from compute_api_client.models.backend_type import BackendType
from compute_api_client.models.page_backend_type import PageBackendType

from compute_api_client.api_client import ApiClient
from compute_api_client.api_response import ApiResponse
from compute_api_client.rest import RESTResponseType


class BackendTypesApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client


    @validate_call
    async def read_backend_type_backend_types_id_get(
        self,
        id: StrictInt,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> BackendType:
        """Retrieve backend type

        Get backend type by ID.

        :param id: (required)
        :type id: int
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._read_backend_type_backend_types_id_get_serialize(
            id=id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "BackendType",
            '404': "HTTPNotFoundError",
            '422': "HTTPValidationError"
            
        }
        response_data = await self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        await response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    async def read_backend_type_backend_types_id_get_with_http_info(
        self,
        id: StrictInt,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[BackendType]:
        """Retrieve backend type

        Get backend type by ID.

        :param id: (required)
        :type id: int
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._read_backend_type_backend_types_id_get_serialize(
            id=id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "BackendType",
            '404': "HTTPNotFoundError",
            '422': "HTTPValidationError"
            
        }
        response_data = await self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        await response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    async def read_backend_type_backend_types_id_get_without_preload_content(
        self,
        id: StrictInt,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Retrieve backend type

        Get backend type by ID.

        :param id: (required)
        :type id: int
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._read_backend_type_backend_types_id_get_serialize(
            id=id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "BackendType",
            '404': "HTTPNotFoundError",
            '422': "HTTPValidationError"
            
        }
        response_data = await self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _read_backend_type_backend_types_id_get_serialize(
        self,
        id,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> Tuple:

        _host = None

        _collection_formats: Dict[str, str] = {
            
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[str, str] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if id is not None:
            _path_params['id'] = id
        # process the query parameters
        # process the header parameters
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            [
                'application/json'
            ]
        )


        # authentication setting
        _auth_settings: List[str] = [
            'user_bearer', 
            'backend'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/backend_types/{id}',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    async def read_backend_types_backend_types_get(
        self,
        id: Optional[StrictInt] = None,
        name: Optional[StrictStr] = None,
        infrastructure: Optional[StrictStr] = None,
        description: Optional[StrictStr] = None,
        image_id: Optional[StrictStr] = None,
        is_hardware: Optional[StrictBool] = None,
        supports_raw_data: Optional[StrictBool] = None,
        nqubits: Optional[StrictInt] = None,
        status: Optional[BackendStatus] = None,
        default_number_of_shots: Optional[StrictInt] = None,
        max_number_of_shots: Optional[StrictInt] = None,
        sort_by: Annotated[Optional[StrictStr], Field(description="The field name to sort on. Prefix with '-' for descending order. E.g., '-created_on'.")] = None,
        latest: Annotated[Optional[StrictBool], Field(description="If True gets the most recently created object.")] = None,
        page: Annotated[Optional[Annotated[int, Field(strict=True, ge=1)]], Field(description="Page number")] = None,
        size: Annotated[Optional[Annotated[int, Field(le=100, strict=True, ge=1)]], Field(description="Page size")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> PageBackendType:
        """List backend types

        Read backend types.

        :param id:
        :type id: int
        :param name:
        :type name: str
        :param infrastructure:
        :type infrastructure: str
        :param description:
        :type description: str
        :param image_id:
        :type image_id: str
        :param is_hardware:
        :type is_hardware: bool
        :param supports_raw_data:
        :type supports_raw_data: bool
        :param nqubits:
        :type nqubits: int
        :param status:
        :type status: BackendStatus
        :param default_number_of_shots:
        :type default_number_of_shots: int
        :param max_number_of_shots:
        :type max_number_of_shots: int
        :param sort_by: The field name to sort on. Prefix with '-' for descending order. E.g., '-created_on'.
        :type sort_by: str
        :param latest: If True gets the most recently created object.
        :type latest: bool
        :param page: Page number
        :type page: int
        :param size: Page size
        :type size: int
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._read_backend_types_backend_types_get_serialize(
            id=id,
            name=name,
            infrastructure=infrastructure,
            description=description,
            image_id=image_id,
            is_hardware=is_hardware,
            supports_raw_data=supports_raw_data,
            nqubits=nqubits,
            status=status,
            default_number_of_shots=default_number_of_shots,
            max_number_of_shots=max_number_of_shots,
            sort_by=sort_by,
            latest=latest,
            page=page,
            size=size,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "PageBackendType",
            '422': "HTTPValidationError"
            
        }
        response_data = await self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        await response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    async def read_backend_types_backend_types_get_with_http_info(
        self,
        id: Optional[StrictInt] = None,
        name: Optional[StrictStr] = None,
        infrastructure: Optional[StrictStr] = None,
        description: Optional[StrictStr] = None,
        image_id: Optional[StrictStr] = None,
        is_hardware: Optional[StrictBool] = None,
        supports_raw_data: Optional[StrictBool] = None,
        nqubits: Optional[StrictInt] = None,
        status: Optional[BackendStatus] = None,
        default_number_of_shots: Optional[StrictInt] = None,
        max_number_of_shots: Optional[StrictInt] = None,
        sort_by: Annotated[Optional[StrictStr], Field(description="The field name to sort on. Prefix with '-' for descending order. E.g., '-created_on'.")] = None,
        latest: Annotated[Optional[StrictBool], Field(description="If True gets the most recently created object.")] = None,
        page: Annotated[Optional[Annotated[int, Field(strict=True, ge=1)]], Field(description="Page number")] = None,
        size: Annotated[Optional[Annotated[int, Field(le=100, strict=True, ge=1)]], Field(description="Page size")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[PageBackendType]:
        """List backend types

        Read backend types.

        :param id:
        :type id: int
        :param name:
        :type name: str
        :param infrastructure:
        :type infrastructure: str
        :param description:
        :type description: str
        :param image_id:
        :type image_id: str
        :param is_hardware:
        :type is_hardware: bool
        :param supports_raw_data:
        :type supports_raw_data: bool
        :param nqubits:
        :type nqubits: int
        :param status:
        :type status: BackendStatus
        :param default_number_of_shots:
        :type default_number_of_shots: int
        :param max_number_of_shots:
        :type max_number_of_shots: int
        :param sort_by: The field name to sort on. Prefix with '-' for descending order. E.g., '-created_on'.
        :type sort_by: str
        :param latest: If True gets the most recently created object.
        :type latest: bool
        :param page: Page number
        :type page: int
        :param size: Page size
        :type size: int
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._read_backend_types_backend_types_get_serialize(
            id=id,
            name=name,
            infrastructure=infrastructure,
            description=description,
            image_id=image_id,
            is_hardware=is_hardware,
            supports_raw_data=supports_raw_data,
            nqubits=nqubits,
            status=status,
            default_number_of_shots=default_number_of_shots,
            max_number_of_shots=max_number_of_shots,
            sort_by=sort_by,
            latest=latest,
            page=page,
            size=size,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "PageBackendType",
            '422': "HTTPValidationError"
            
        }
        response_data = await self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        await response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    async def read_backend_types_backend_types_get_without_preload_content(
        self,
        id: Optional[StrictInt] = None,
        name: Optional[StrictStr] = None,
        infrastructure: Optional[StrictStr] = None,
        description: Optional[StrictStr] = None,
        image_id: Optional[StrictStr] = None,
        is_hardware: Optional[StrictBool] = None,
        supports_raw_data: Optional[StrictBool] = None,
        nqubits: Optional[StrictInt] = None,
        status: Optional[BackendStatus] = None,
        default_number_of_shots: Optional[StrictInt] = None,
        max_number_of_shots: Optional[StrictInt] = None,
        sort_by: Annotated[Optional[StrictStr], Field(description="The field name to sort on. Prefix with '-' for descending order. E.g., '-created_on'.")] = None,
        latest: Annotated[Optional[StrictBool], Field(description="If True gets the most recently created object.")] = None,
        page: Annotated[Optional[Annotated[int, Field(strict=True, ge=1)]], Field(description="Page number")] = None,
        size: Annotated[Optional[Annotated[int, Field(le=100, strict=True, ge=1)]], Field(description="Page size")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """List backend types

        Read backend types.

        :param id:
        :type id: int
        :param name:
        :type name: str
        :param infrastructure:
        :type infrastructure: str
        :param description:
        :type description: str
        :param image_id:
        :type image_id: str
        :param is_hardware:
        :type is_hardware: bool
        :param supports_raw_data:
        :type supports_raw_data: bool
        :param nqubits:
        :type nqubits: int
        :param status:
        :type status: BackendStatus
        :param default_number_of_shots:
        :type default_number_of_shots: int
        :param max_number_of_shots:
        :type max_number_of_shots: int
        :param sort_by: The field name to sort on. Prefix with '-' for descending order. E.g., '-created_on'.
        :type sort_by: str
        :param latest: If True gets the most recently created object.
        :type latest: bool
        :param page: Page number
        :type page: int
        :param size: Page size
        :type size: int
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._read_backend_types_backend_types_get_serialize(
            id=id,
            name=name,
            infrastructure=infrastructure,
            description=description,
            image_id=image_id,
            is_hardware=is_hardware,
            supports_raw_data=supports_raw_data,
            nqubits=nqubits,
            status=status,
            default_number_of_shots=default_number_of_shots,
            max_number_of_shots=max_number_of_shots,
            sort_by=sort_by,
            latest=latest,
            page=page,
            size=size,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "PageBackendType",
            '422': "HTTPValidationError"
            
        }
        response_data = await self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _read_backend_types_backend_types_get_serialize(
        self,
        id,
        name,
        infrastructure,
        description,
        image_id,
        is_hardware,
        supports_raw_data,
        nqubits,
        status,
        default_number_of_shots,
        max_number_of_shots,
        sort_by,
        latest,
        page,
        size,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> Tuple:

        _host = None

        _collection_formats: Dict[str, str] = {
            
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[str, str] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        # process the query parameters
        if id is not None:
            
            _query_params.append(('id', id))
            
        if name is not None:
            
            _query_params.append(('name', name))
            
        if infrastructure is not None:
            
            _query_params.append(('infrastructure', infrastructure))
            
        if description is not None:
            
            _query_params.append(('description', description))
            
        if image_id is not None:
            
            _query_params.append(('image_id', image_id))
            
        if is_hardware is not None:
            
            _query_params.append(('is_hardware', is_hardware))
            
        if supports_raw_data is not None:
            
            _query_params.append(('supports_raw_data', supports_raw_data))
            
        if nqubits is not None:
            
            _query_params.append(('nqubits', nqubits))
            
        if status is not None:
            
            _query_params.append(('status', status.value))
            
        if default_number_of_shots is not None:
            
            _query_params.append(('default_number_of_shots', default_number_of_shots))
            
        if max_number_of_shots is not None:
            
            _query_params.append(('max_number_of_shots', max_number_of_shots))
            
        if sort_by is not None:
            
            _query_params.append(('sort_by', sort_by))
            
        if latest is not None:
            
            _query_params.append(('latest', latest))
            
        if page is not None:
            
            _query_params.append(('page', page))
            
        if size is not None:
            
            _query_params.append(('size', size))
            
        # process the header parameters
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            [
                'application/json'
            ]
        )


        # authentication setting
        _auth_settings: List[str] = [
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/backend_types/',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )


