# coding: utf-8

"""
    Quantum Inspire 2

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.1.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from compute_api_client.api_client import ApiClient
from compute_api_client.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class BackendTypesApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def read_backend_type_backend_types_id_get(self, id, **kwargs):  # noqa: E501
        """Retrieve backend type  # noqa: E501

        Get backend type by ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.read_backend_type_backend_types_id_get(id, async_req=True)
        >>> result = thread.get()

        :param id: (required)
        :type id: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: BackendType
        """
        kwargs['_return_http_data_only'] = True
        return self.read_backend_type_backend_types_id_get_with_http_info(id, **kwargs)  # noqa: E501

    def read_backend_type_backend_types_id_get_with_http_info(self, id, **kwargs):  # noqa: E501
        """Retrieve backend type  # noqa: E501

        Get backend type by ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.read_backend_type_backend_types_id_get_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param id: (required)
        :type id: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(BackendType, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'id'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method read_backend_type_backend_types_id_get" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and local_var_params.get('id') is None:  # noqa: E501
            raise ApiValueError("Missing the required parameter `id` when calling `read_backend_type_backend_types_id_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']  # noqa: E501

        query_params = []

        header_params = dict(local_var_params.get('_headers', {}))

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['user']  # noqa: E501

        response_types_map = {
            200: "BackendType",
            404: "HTTPNotFoundError",
            422: "HTTPValidationError",
        }

        return self.api_client.call_api(
            '/backend_types/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_types_map=response_types_map,
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def read_backend_types_backend_types_get(self, **kwargs):  # noqa: E501
        """List backend types  # noqa: E501

        Read backend types.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.read_backend_types_backend_types_get(async_req=True)
        >>> result = thread.get()

        :param latest:
        :type latest: bool
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
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: list[BackendType]
        """
        kwargs['_return_http_data_only'] = True
        return self.read_backend_types_backend_types_get_with_http_info(**kwargs)  # noqa: E501

    def read_backend_types_backend_types_get_with_http_info(self, **kwargs):  # noqa: E501
        """List backend types  # noqa: E501

        Read backend types.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.read_backend_types_backend_types_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param latest:
        :type latest: bool
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
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(list[BackendType], status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'latest',
            'id',
            'name',
            'infrastructure',
            'description',
            'image_id',
            'is_hardware'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method read_backend_types_backend_types_get" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if local_var_params.get('latest') is not None:  # noqa: E501
            query_params.append(('latest', local_var_params['latest']))  # noqa: E501
        if local_var_params.get('id') is not None:  # noqa: E501
            query_params.append(('id', local_var_params['id']))  # noqa: E501
        if local_var_params.get('name') is not None:  # noqa: E501
            query_params.append(('name', local_var_params['name']))  # noqa: E501
        if local_var_params.get('infrastructure') is not None:  # noqa: E501
            query_params.append(('infrastructure', local_var_params['infrastructure']))  # noqa: E501
        if local_var_params.get('description') is not None:  # noqa: E501
            query_params.append(('description', local_var_params['description']))  # noqa: E501
        if local_var_params.get('image_id') is not None:  # noqa: E501
            query_params.append(('image_id', local_var_params['image_id']))  # noqa: E501
        if local_var_params.get('is_hardware') is not None:  # noqa: E501
            query_params.append(('is_hardware', local_var_params['is_hardware']))  # noqa: E501

        header_params = dict(local_var_params.get('_headers', {}))

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['user']  # noqa: E501

        response_types_map = {
            200: "list[BackendType]",
            422: "HTTPValidationError",
        }

        return self.api_client.call_api(
            '/backend_types/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_types_map=response_types_map,
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))
