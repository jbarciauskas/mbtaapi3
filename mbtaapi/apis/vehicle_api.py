# coding: utf-8

"""
    MBTA

    MBTA service API. https://www.mbta.com

    OpenAPI spec version: 3.0
    Contact: developer@mbta.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class VehicleApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def api_web_vehicle_controller_index(self, **kwargs):
        """
        
        List of vehicles (buses, ferries, and trains)  ## Direction  ### World  To figure out which way the vehicle is pointing at the location, use `/data/{index}/attributes/bearing`.  This can be the compass bearing, or the direction towards the next stop or intermediate location.  ### Trip  To get the direction around the stops in the trip use `/data/{index}/attributes/direction_id`.  ## Location  ### World  Use `/data/{index}/attributes/latitude` and `/data/{index}/attributes/longitude` to get the location of a vehicle.  ### Trip  Use `/data/{index}/attributes/current_stop_sequence` to get the stop number along the trip.  Useful for linear stop indicators.  Position relative to the current stop is in `/data/{index}/attributes/current_status`.  ## Movement  ### World  Use `/data/{index}/attributes/speed` to get the speed of the vehicle in meters per second.  
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.api_web_vehicle_controller_index(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int page_offset: Offset (0-based) of first element in the page
        :param int page_limit: Max number of elements to return
        :param str sort: Results can be [sorted](http://jsonapi.org/format/#fetching-sorting) by the id or any `/data/{index}/attributes` key. Assumes ascending; may be prefixed with '-' for descending  | JSON pointer | Direction | `sort`     | |--------------|-----------|------------| | `/data/{index}/attributes/bearing` | ascending | `bearing` | | `/data/{index}/attributes/bearing` | descending | `-bearing` | | `/data/{index}/attributes/current_status` | ascending | `current_status` | | `/data/{index}/attributes/current_status` | descending | `-current_status` | | `/data/{index}/attributes/current_stop_sequence` | ascending | `current_stop_sequence` | | `/data/{index}/attributes/current_stop_sequence` | descending | `-current_stop_sequence` | | `/data/{index}/attributes/direction_id` | ascending | `direction_id` | | `/data/{index}/attributes/direction_id` | descending | `-direction_id` | | `/data/{index}/attributes/label` | ascending | `label` | | `/data/{index}/attributes/label` | descending | `-label` | | `/data/{index}/attributes/last_updated` | ascending | `last_updated` | | `/data/{index}/attributes/last_updated` | descending | `-last_updated` | | `/data/{index}/attributes/latitude` | ascending | `latitude` | | `/data/{index}/attributes/latitude` | descending | `-latitude` | | `/data/{index}/attributes/longitude` | ascending | `longitude` | | `/data/{index}/attributes/longitude` | descending | `-longitude` | | `/data/{index}/attributes/speed` | ascending | `speed` | | `/data/{index}/attributes/speed` | descending | `-speed` |  
        :param str api_key: Key for API access.  Without api_key, requests will be tracked by IP address and have stricter rate limit. [Register for a key](/register) 
        :param str include: Relationships to include.  * `trip` * `stop` * `route`  The value of the include parameter **MUST** be a comma-separated (U+002C COMMA, \",\") list of relationship paths. A relationship path is a dot-separated (U+002E FULL-STOP, \".\") list of relationship names. [JSONAPI \"include\" behavior](http://jsonapi.org/format/#fetching-includes)  | include | Description                                                                                                                                                                                                                                                                                                                                                  | |---------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| | `trip`  | The trip which the vehicle is currently operating.                                                                                                                                                                                                                                                                                                           | | `stop`  | The vehicle's current (when `current_status` is **STOPPED_AT**) or *next* stop.                                                                                                                                                                                                                                                                              | | `route` | The one route that is designated for that trip, as in GTFS `trips.txt`.  A trip might also provide service on other routes, identified by the MBTA's `multi_route_trips.txt` GTFS extension. `filter[route]` does consider the multi_route_trips GTFS extension, so it is possible to filter for one route and get a different route included in the response. |  
        :param str filter_trip: Filter by `/data/{index}/relationships/trip/data/id`. Multiple `/data/{index}/relationships/trip/data/id` **MUST** be a comma-separated (U+002C COMMA, \",\") list.
        :param str filter_route: Filter by route. If the vehicle is on a [multi-route trip](https://groups.google.com/forum/#!msg/massdotdevelopers/1egrhNjT9eA/iy6NFymcCgAJ), it will be returned for any of the routes. Multiple `route_id` **MUST** be a comma-separated (U+002C COMMA, \",\") list. 
        :param str filter_direction_id: Filter by direction of travel along the route.  The meaning of `direction_id` varies based on the route. You can programmatically get the direction names from `/routes` `/data/{index}/attributes/direction_names` or `/routes/{id}` `/data/attributes/direction_names`.    
        :return: Vehicles
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.api_web_vehicle_controller_index_with_http_info(**kwargs)
        else:
            (data) = self.api_web_vehicle_controller_index_with_http_info(**kwargs)
            return data

    def api_web_vehicle_controller_index_with_http_info(self, **kwargs):
        """
        
        List of vehicles (buses, ferries, and trains)  ## Direction  ### World  To figure out which way the vehicle is pointing at the location, use `/data/{index}/attributes/bearing`.  This can be the compass bearing, or the direction towards the next stop or intermediate location.  ### Trip  To get the direction around the stops in the trip use `/data/{index}/attributes/direction_id`.  ## Location  ### World  Use `/data/{index}/attributes/latitude` and `/data/{index}/attributes/longitude` to get the location of a vehicle.  ### Trip  Use `/data/{index}/attributes/current_stop_sequence` to get the stop number along the trip.  Useful for linear stop indicators.  Position relative to the current stop is in `/data/{index}/attributes/current_status`.  ## Movement  ### World  Use `/data/{index}/attributes/speed` to get the speed of the vehicle in meters per second.  
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.api_web_vehicle_controller_index_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int page_offset: Offset (0-based) of first element in the page
        :param int page_limit: Max number of elements to return
        :param str sort: Results can be [sorted](http://jsonapi.org/format/#fetching-sorting) by the id or any `/data/{index}/attributes` key. Assumes ascending; may be prefixed with '-' for descending  | JSON pointer | Direction | `sort`     | |--------------|-----------|------------| | `/data/{index}/attributes/bearing` | ascending | `bearing` | | `/data/{index}/attributes/bearing` | descending | `-bearing` | | `/data/{index}/attributes/current_status` | ascending | `current_status` | | `/data/{index}/attributes/current_status` | descending | `-current_status` | | `/data/{index}/attributes/current_stop_sequence` | ascending | `current_stop_sequence` | | `/data/{index}/attributes/current_stop_sequence` | descending | `-current_stop_sequence` | | `/data/{index}/attributes/direction_id` | ascending | `direction_id` | | `/data/{index}/attributes/direction_id` | descending | `-direction_id` | | `/data/{index}/attributes/label` | ascending | `label` | | `/data/{index}/attributes/label` | descending | `-label` | | `/data/{index}/attributes/last_updated` | ascending | `last_updated` | | `/data/{index}/attributes/last_updated` | descending | `-last_updated` | | `/data/{index}/attributes/latitude` | ascending | `latitude` | | `/data/{index}/attributes/latitude` | descending | `-latitude` | | `/data/{index}/attributes/longitude` | ascending | `longitude` | | `/data/{index}/attributes/longitude` | descending | `-longitude` | | `/data/{index}/attributes/speed` | ascending | `speed` | | `/data/{index}/attributes/speed` | descending | `-speed` |  
        :param str api_key: Key for API access.  Without api_key, requests will be tracked by IP address and have stricter rate limit. [Register for a key](/register) 
        :param str include: Relationships to include.  * `trip` * `stop` * `route`  The value of the include parameter **MUST** be a comma-separated (U+002C COMMA, \",\") list of relationship paths. A relationship path is a dot-separated (U+002E FULL-STOP, \".\") list of relationship names. [JSONAPI \"include\" behavior](http://jsonapi.org/format/#fetching-includes)  | include | Description                                                                                                                                                                                                                                                                                                                                                  | |---------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| | `trip`  | The trip which the vehicle is currently operating.                                                                                                                                                                                                                                                                                                           | | `stop`  | The vehicle's current (when `current_status` is **STOPPED_AT**) or *next* stop.                                                                                                                                                                                                                                                                              | | `route` | The one route that is designated for that trip, as in GTFS `trips.txt`.  A trip might also provide service on other routes, identified by the MBTA's `multi_route_trips.txt` GTFS extension. `filter[route]` does consider the multi_route_trips GTFS extension, so it is possible to filter for one route and get a different route included in the response. |  
        :param str filter_trip: Filter by `/data/{index}/relationships/trip/data/id`. Multiple `/data/{index}/relationships/trip/data/id` **MUST** be a comma-separated (U+002C COMMA, \",\") list.
        :param str filter_route: Filter by route. If the vehicle is on a [multi-route trip](https://groups.google.com/forum/#!msg/massdotdevelopers/1egrhNjT9eA/iy6NFymcCgAJ), it will be returned for any of the routes. Multiple `route_id` **MUST** be a comma-separated (U+002C COMMA, \",\") list. 
        :param str filter_direction_id: Filter by direction of travel along the route.  The meaning of `direction_id` varies based on the route. You can programmatically get the direction names from `/routes` `/data/{index}/attributes/direction_names` or `/routes/{id}` `/data/attributes/direction_names`.    
        :return: Vehicles
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['page_offset', 'page_limit', 'sort', 'api_key', 'include', 'filter_trip', 'filter_route', 'filter_direction_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_web_vehicle_controller_index" % key
                )
            params[key] = val
        del params['kwargs']

        if 'page_offset' in params and params['page_offset'] < 0:
            raise ValueError("Invalid value for parameter `page_offset` when calling `api_web_vehicle_controller_index`, must be a value greater than or equal to `0`")
        if 'page_limit' in params and params['page_limit'] < 1:
            raise ValueError("Invalid value for parameter `page_limit` when calling `api_web_vehicle_controller_index`, must be a value greater than or equal to `1`")

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'page_offset' in params:
            query_params.append(('page[offset]', params['page_offset']))
        if 'page_limit' in params:
            query_params.append(('page[limit]', params['page_limit']))
        if 'sort' in params:
            query_params.append(('sort', params['sort']))
        if 'api_key' in params:
            query_params.append(('api_key', params['api_key']))
        if 'include' in params:
            query_params.append(('include', params['include']))
        if 'filter_trip' in params:
            query_params.append(('filter[trip]', params['filter_trip']))
        if 'filter_route' in params:
            query_params.append(('filter[route]', params['filter_route']))
        if 'filter_direction_id' in params:
            query_params.append(('filter[direction_id]', params['filter_direction_id']))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/vnd.api+json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/vnd.api+json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/vehicles', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='Vehicles',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def api_web_vehicle_controller_show(self, id, **kwargs):
        """
        
        Single vehicle (bus, ferry, or train)  ## Direction  ### World  To figure out which way the vehicle is pointing at the location, use `/data/attributes/bearing`.  This can be the compass bearing, or the direction towards the next stop or intermediate location.  ### Trip  To get the direction around the stops in the trip use `/data/attributes/direction_id`.  ## Location  ### World  Use `/data/attributes/latitude` and `/data/attributes/longitude` to get the location of a vehicle.  ### Trip  Use `/data/attributes/current_stop_sequence` to get the stop number along the trip.  Useful for linear stop indicators.  Position relative to the current stop is in `/data/attributes/current_status`.  ## Movement  ### World  Use `/data/attributes/speed` to get the speed of the vehicle in meters per second.  
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.api_web_vehicle_controller_show(id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str id: Unique identifier for a vehicle (required)
        :param str api_key: Key for API access.  Without api_key, requests will be tracked by IP address and have stricter rate limit. [Register for a key](/register) 
        :param str include: Relationships to include.  * `trip` * `stop` * `route`  The value of the include parameter **MUST** be a comma-separated (U+002C COMMA, \",\") list of relationship paths. A relationship path is a dot-separated (U+002E FULL-STOP, \".\") list of relationship names. [JSONAPI \"include\" behavior](http://jsonapi.org/format/#fetching-includes)  | include | Description                                                                                                                                                                                                                                                                                                                                                  | |---------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| | `trip`  | The trip which the vehicle is currently operating.                                                                                                                                                                                                                                                                                                           | | `stop`  | The vehicle's current (when `current_status` is **STOPPED_AT**) or *next* stop.                                                                                                                                                                                                                                                                              | | `route` | The one route that is designated for that trip, as in GTFS `trips.txt`.  A trip might also provide service on other routes, identified by the MBTA's `multi_route_trips.txt` GTFS extension. `filter[route]` does consider the multi_route_trips GTFS extension, so it is possible to filter for one route and get a different route included in the response. |  
        :return: Vehicle
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.api_web_vehicle_controller_show_with_http_info(id, **kwargs)
        else:
            (data) = self.api_web_vehicle_controller_show_with_http_info(id, **kwargs)
            return data

    def api_web_vehicle_controller_show_with_http_info(self, id, **kwargs):
        """
        
        Single vehicle (bus, ferry, or train)  ## Direction  ### World  To figure out which way the vehicle is pointing at the location, use `/data/attributes/bearing`.  This can be the compass bearing, or the direction towards the next stop or intermediate location.  ### Trip  To get the direction around the stops in the trip use `/data/attributes/direction_id`.  ## Location  ### World  Use `/data/attributes/latitude` and `/data/attributes/longitude` to get the location of a vehicle.  ### Trip  Use `/data/attributes/current_stop_sequence` to get the stop number along the trip.  Useful for linear stop indicators.  Position relative to the current stop is in `/data/attributes/current_status`.  ## Movement  ### World  Use `/data/attributes/speed` to get the speed of the vehicle in meters per second.  
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.api_web_vehicle_controller_show_with_http_info(id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str id: Unique identifier for a vehicle (required)
        :param str api_key: Key for API access.  Without api_key, requests will be tracked by IP address and have stricter rate limit. [Register for a key](/register) 
        :param str include: Relationships to include.  * `trip` * `stop` * `route`  The value of the include parameter **MUST** be a comma-separated (U+002C COMMA, \",\") list of relationship paths. A relationship path is a dot-separated (U+002E FULL-STOP, \".\") list of relationship names. [JSONAPI \"include\" behavior](http://jsonapi.org/format/#fetching-includes)  | include | Description                                                                                                                                                                                                                                                                                                                                                  | |---------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| | `trip`  | The trip which the vehicle is currently operating.                                                                                                                                                                                                                                                                                                           | | `stop`  | The vehicle's current (when `current_status` is **STOPPED_AT**) or *next* stop.                                                                                                                                                                                                                                                                              | | `route` | The one route that is designated for that trip, as in GTFS `trips.txt`.  A trip might also provide service on other routes, identified by the MBTA's `multi_route_trips.txt` GTFS extension. `filter[route]` does consider the multi_route_trips GTFS extension, so it is possible to filter for one route and get a different route included in the response. |  
        :return: Vehicle
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'api_key', 'include']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_web_vehicle_controller_show" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `api_web_vehicle_controller_show`")


        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']

        query_params = []
        if 'api_key' in params:
            query_params.append(('api_key', params['api_key']))
        if 'include' in params:
            query_params.append(('include', params['include']))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/vnd.api+json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/vnd.api+json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/vehicles/{id}', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='Vehicle',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)