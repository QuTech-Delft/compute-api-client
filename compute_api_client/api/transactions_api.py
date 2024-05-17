# coding: utf-8

"""
    Quantum Inspire 2

     **Sorting and Pagination of list endpoints**  The api provides sorting and pagination for list endpoints. The following parameters can be passed as query parameters to get sorted and paginated list.  - `latest`     - **Type**: Boolean.     - **Description**: Get the most recently created object. Defaults to False. - `sort_by`     - **Type**: String:     - **Description**: The field / column name to sort on. To reverse sort provide the field with a \"-\" sign. E.g. \"created_on\" for ascending order while \"-created_on\" in descending order. Defaults to \"id\". - `page_number`     - **Type**: Positive Integer     - **Description**: The page number for pagination. Defaults to 1. - `items_per_page`     - **Type**: Positive Integer.     - **Description**: The number of items per page for pagination. Defaults to 50. 

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

from datetime import datetime

from pydantic import StrictBool, StrictInt, StrictStr

from typing import List, Optional

from compute_api_client.models.domain import Domain
from compute_api_client.models.transaction import Transaction

from compute_api_client.api_client import ApiClient
from compute_api_client.api_response import ApiResponse
from compute_api_client.rest import RESTResponseType


class TransactionsApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client


    @validate_call
    async def read_transaction_transactions_id_get(
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
    ) -> Transaction:
        """Retrieve transactions

        Get transaction by ID.

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

        _param = self._read_transaction_transactions_id_get_serialize(
            id=id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "Transaction",
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
    async def read_transaction_transactions_id_get_with_http_info(
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
    ) -> ApiResponse[Transaction]:
        """Retrieve transactions

        Get transaction by ID.

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

        _param = self._read_transaction_transactions_id_get_serialize(
            id=id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "Transaction",
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
    async def read_transaction_transactions_id_get_without_preload_content(
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
        """Retrieve transactions

        Get transaction by ID.

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

        _param = self._read_transaction_transactions_id_get_serialize(
            id=id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "Transaction",
            '404': "HTTPNotFoundError",
            '422': "HTTPValidationError"
            
        }
        response_data = await self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _read_transaction_transactions_id_get_serialize(
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
            'user_bearer'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/transactions/{id}',
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
    async def read_transactions_transactions_get(
        self,
        latest: Optional[StrictBool] = None,
        sort_by: Optional[StrictStr] = None,
        page_number: Optional[StrictInt] = None,
        items_per_page: Optional[StrictInt] = None,
        id: Optional[StrictInt] = None,
        domain__isnull: Optional[StrictBool] = None,
        domain: Optional[Domain] = None,
        job__isnull: Optional[StrictBool] = None,
        job: Optional[StrictInt] = None,
        team_id: Optional[StrictInt] = None,
        member_id__isnull: Optional[StrictBool] = None,
        member_id: Optional[StrictInt] = None,
        change: Optional[StrictInt] = None,
        timestamp: Optional[datetime] = None,
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
    ) -> List[Transaction]:
        """List transactions

        Read transactions.

        :param latest:
        :type latest: bool
        :param sort_by:
        :type sort_by: str
        :param page_number:
        :type page_number: int
        :param items_per_page:
        :type items_per_page: int
        :param id:
        :type id: int
        :param domain__isnull:
        :type domain__isnull: bool
        :param domain:
        :type domain: Domain
        :param job__isnull:
        :type job__isnull: bool
        :param job:
        :type job: int
        :param team_id:
        :type team_id: int
        :param member_id__isnull:
        :type member_id__isnull: bool
        :param member_id:
        :type member_id: int
        :param change:
        :type change: int
        :param timestamp:
        :type timestamp: datetime
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

        _param = self._read_transactions_transactions_get_serialize(
            latest=latest,
            sort_by=sort_by,
            page_number=page_number,
            items_per_page=items_per_page,
            id=id,
            domain__isnull=domain__isnull,
            domain=domain,
            job__isnull=job__isnull,
            job=job,
            team_id=team_id,
            member_id__isnull=member_id__isnull,
            member_id=member_id,
            change=change,
            timestamp=timestamp,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "List[Transaction]",
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
    async def read_transactions_transactions_get_with_http_info(
        self,
        latest: Optional[StrictBool] = None,
        sort_by: Optional[StrictStr] = None,
        page_number: Optional[StrictInt] = None,
        items_per_page: Optional[StrictInt] = None,
        id: Optional[StrictInt] = None,
        domain__isnull: Optional[StrictBool] = None,
        domain: Optional[Domain] = None,
        job__isnull: Optional[StrictBool] = None,
        job: Optional[StrictInt] = None,
        team_id: Optional[StrictInt] = None,
        member_id__isnull: Optional[StrictBool] = None,
        member_id: Optional[StrictInt] = None,
        change: Optional[StrictInt] = None,
        timestamp: Optional[datetime] = None,
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
    ) -> ApiResponse[List[Transaction]]:
        """List transactions

        Read transactions.

        :param latest:
        :type latest: bool
        :param sort_by:
        :type sort_by: str
        :param page_number:
        :type page_number: int
        :param items_per_page:
        :type items_per_page: int
        :param id:
        :type id: int
        :param domain__isnull:
        :type domain__isnull: bool
        :param domain:
        :type domain: Domain
        :param job__isnull:
        :type job__isnull: bool
        :param job:
        :type job: int
        :param team_id:
        :type team_id: int
        :param member_id__isnull:
        :type member_id__isnull: bool
        :param member_id:
        :type member_id: int
        :param change:
        :type change: int
        :param timestamp:
        :type timestamp: datetime
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

        _param = self._read_transactions_transactions_get_serialize(
            latest=latest,
            sort_by=sort_by,
            page_number=page_number,
            items_per_page=items_per_page,
            id=id,
            domain__isnull=domain__isnull,
            domain=domain,
            job__isnull=job__isnull,
            job=job,
            team_id=team_id,
            member_id__isnull=member_id__isnull,
            member_id=member_id,
            change=change,
            timestamp=timestamp,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "List[Transaction]",
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
    async def read_transactions_transactions_get_without_preload_content(
        self,
        latest: Optional[StrictBool] = None,
        sort_by: Optional[StrictStr] = None,
        page_number: Optional[StrictInt] = None,
        items_per_page: Optional[StrictInt] = None,
        id: Optional[StrictInt] = None,
        domain__isnull: Optional[StrictBool] = None,
        domain: Optional[Domain] = None,
        job__isnull: Optional[StrictBool] = None,
        job: Optional[StrictInt] = None,
        team_id: Optional[StrictInt] = None,
        member_id__isnull: Optional[StrictBool] = None,
        member_id: Optional[StrictInt] = None,
        change: Optional[StrictInt] = None,
        timestamp: Optional[datetime] = None,
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
        """List transactions

        Read transactions.

        :param latest:
        :type latest: bool
        :param sort_by:
        :type sort_by: str
        :param page_number:
        :type page_number: int
        :param items_per_page:
        :type items_per_page: int
        :param id:
        :type id: int
        :param domain__isnull:
        :type domain__isnull: bool
        :param domain:
        :type domain: Domain
        :param job__isnull:
        :type job__isnull: bool
        :param job:
        :type job: int
        :param team_id:
        :type team_id: int
        :param member_id__isnull:
        :type member_id__isnull: bool
        :param member_id:
        :type member_id: int
        :param change:
        :type change: int
        :param timestamp:
        :type timestamp: datetime
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

        _param = self._read_transactions_transactions_get_serialize(
            latest=latest,
            sort_by=sort_by,
            page_number=page_number,
            items_per_page=items_per_page,
            id=id,
            domain__isnull=domain__isnull,
            domain=domain,
            job__isnull=job__isnull,
            job=job,
            team_id=team_id,
            member_id__isnull=member_id__isnull,
            member_id=member_id,
            change=change,
            timestamp=timestamp,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "List[Transaction]",
            '422': "HTTPValidationError"
            
        }
        response_data = await self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _read_transactions_transactions_get_serialize(
        self,
        latest,
        sort_by,
        page_number,
        items_per_page,
        id,
        domain__isnull,
        domain,
        job__isnull,
        job,
        team_id,
        member_id__isnull,
        member_id,
        change,
        timestamp,
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
        if latest is not None:
            
            _query_params.append(('latest', latest))
            
        if sort_by is not None:
            
            _query_params.append(('sort_by', sort_by))
            
        if page_number is not None:
            
            _query_params.append(('page_number', page_number))
            
        if items_per_page is not None:
            
            _query_params.append(('items_per_page', items_per_page))
            
        if id is not None:
            
            _query_params.append(('id', id))
            
        if domain__isnull is not None:
            
            _query_params.append(('domain__isnull', domain__isnull))
            
        if domain is not None:
            
            _query_params.append(('domain', domain.value))
            
        if job__isnull is not None:
            
            _query_params.append(('job__isnull', job__isnull))
            
        if job is not None:
            
            _query_params.append(('job', job))
            
        if team_id is not None:
            
            _query_params.append(('team_id', team_id))
            
        if member_id__isnull is not None:
            
            _query_params.append(('member_id__isnull', member_id__isnull))
            
        if member_id is not None:
            
            _query_params.append(('member_id', member_id))
            
        if change is not None:
            
            _query_params.append(('change', change))
            
        if timestamp is not None:
            if isinstance(timestamp, datetime):
                _query_params.append(
                    (
                        'timestamp',
                        timestamp.strftime(
                            self.api_client.configuration.datetime_format
                        )
                    )
                )
            else:
                _query_params.append(('timestamp', timestamp))
            
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
            'user_bearer'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/transactions/',
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


