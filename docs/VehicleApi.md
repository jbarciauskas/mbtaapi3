# mbtaapi.VehicleApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_web_vehicle_controller_index**](VehicleApi.md#api_web_vehicle_controller_index) | **GET** /vehicles | 
[**api_web_vehicle_controller_show**](VehicleApi.md#api_web_vehicle_controller_show) | **GET** /vehicles/{id} | 


# **api_web_vehicle_controller_index**
> Vehicles api_web_vehicle_controller_index(page_offset=page_offset, page_limit=page_limit, sort=sort, api_key=api_key, include=include, filter_trip=filter_trip, filter_route=filter_route, filter_direction_id=filter_direction_id)



List of vehicles (buses, ferries, and trains)  ## Direction  ### World  To figure out which way the vehicle is pointing at the location, use `/data/{index}/attributes/bearing`.  This can be the compass bearing, or the direction towards the next stop or intermediate location.  ### Trip  To get the direction around the stops in the trip use `/data/{index}/attributes/direction_id`.  ## Location  ### World  Use `/data/{index}/attributes/latitude` and `/data/{index}/attributes/longitude` to get the location of a vehicle.  ### Trip  Use `/data/{index}/attributes/current_stop_sequence` to get the stop number along the trip.  Useful for linear stop indicators.  Position relative to the current stop is in `/data/{index}/attributes/current_status`.  ## Movement  ### World  Use `/data/{index}/attributes/speed` to get the speed of the vehicle in meters per second.  

### Example 
```python
from __future__ import print_function
import time
import mbtaapi
from mbtaapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mbtaapi.VehicleApi()
page_offset = 56 # int | Offset (0-based) of first element in the page (optional)
page_limit = 56 # int | Max number of elements to return (optional)
sort = 'sort_example' # str | Results can be [sorted](http://jsonapi.org/format/#fetching-sorting) by the id or any `/data/{index}/attributes` key. Assumes ascending; may be prefixed with '-' for descending  | JSON pointer | Direction | `sort`     | |--------------|-----------|------------| | `/data/{index}/attributes/bearing` | ascending | `bearing` | | `/data/{index}/attributes/bearing` | descending | `-bearing` | | `/data/{index}/attributes/current_status` | ascending | `current_status` | | `/data/{index}/attributes/current_status` | descending | `-current_status` | | `/data/{index}/attributes/current_stop_sequence` | ascending | `current_stop_sequence` | | `/data/{index}/attributes/current_stop_sequence` | descending | `-current_stop_sequence` | | `/data/{index}/attributes/direction_id` | ascending | `direction_id` | | `/data/{index}/attributes/direction_id` | descending | `-direction_id` | | `/data/{index}/attributes/label` | ascending | `label` | | `/data/{index}/attributes/label` | descending | `-label` | | `/data/{index}/attributes/last_updated` | ascending | `last_updated` | | `/data/{index}/attributes/last_updated` | descending | `-last_updated` | | `/data/{index}/attributes/latitude` | ascending | `latitude` | | `/data/{index}/attributes/latitude` | descending | `-latitude` | | `/data/{index}/attributes/longitude` | ascending | `longitude` | | `/data/{index}/attributes/longitude` | descending | `-longitude` | | `/data/{index}/attributes/speed` | ascending | `speed` | | `/data/{index}/attributes/speed` | descending | `-speed` |   (optional)
api_key = 'api_key_example' # str | Key for API access.  Without api_key, requests will be tracked by IP address and have stricter rate limit. [Register for a key](/register)  (optional)
include = 'include_example' # str | Relationships to include.  * `trip` * `stop` * `route`  The value of the include parameter **MUST** be a comma-separated (U+002C COMMA, \",\") list of relationship paths. A relationship path is a dot-separated (U+002E FULL-STOP, \".\") list of relationship names. [JSONAPI \"include\" behavior](http://jsonapi.org/format/#fetching-includes)  | include | Description                                                                                                                                                                                                                                                                                                                                                  | |---------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| | `trip`  | The trip which the vehicle is currently operating.                                                                                                                                                                                                                                                                                                           | | `stop`  | The vehicle's current (when `current_status` is **STOPPED_AT**) or *next* stop.                                                                                                                                                                                                                                                                              | | `route` | The one route that is designated for that trip, as in GTFS `trips.txt`.  A trip might also provide service on other routes, identified by the MBTA's `multi_route_trips.txt` GTFS extension. `filter[route]` does consider the multi_route_trips GTFS extension, so it is possible to filter for one route and get a different route included in the response. |   (optional)
filter_trip = 'filter_trip_example' # str | Filter by `/data/{index}/relationships/trip/data/id`. Multiple `/data/{index}/relationships/trip/data/id` **MUST** be a comma-separated (U+002C COMMA, \",\") list. (optional)
filter_route = 'filter_route_example' # str | Filter by route. If the vehicle is on a [multi-route trip](https://groups.google.com/forum/#!msg/massdotdevelopers/1egrhNjT9eA/iy6NFymcCgAJ), it will be returned for any of the routes. Multiple `route_id` **MUST** be a comma-separated (U+002C COMMA, \",\") list.  (optional)
filter_direction_id = 'filter_direction_id_example' # str | Filter by direction of travel along the route.  The meaning of `direction_id` varies based on the route. You can programmatically get the direction names from `/routes` `/data/{index}/attributes/direction_names` or `/routes/{id}` `/data/attributes/direction_names`.     (optional)

try: 
    # 
    api_response = api_instance.api_web_vehicle_controller_index(page_offset=page_offset, page_limit=page_limit, sort=sort, api_key=api_key, include=include, filter_trip=filter_trip, filter_route=filter_route, filter_direction_id=filter_direction_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VehicleApi->api_web_vehicle_controller_index: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_offset** | **int**| Offset (0-based) of first element in the page | [optional] 
 **page_limit** | **int**| Max number of elements to return | [optional] 
 **sort** | **str**| Results can be [sorted](http://jsonapi.org/format/#fetching-sorting) by the id or any &#x60;/data/{index}/attributes&#x60; key. Assumes ascending; may be prefixed with &#39;-&#39; for descending  | JSON pointer | Direction | &#x60;sort&#x60;     | |--------------|-----------|------------| | &#x60;/data/{index}/attributes/bearing&#x60; | ascending | &#x60;bearing&#x60; | | &#x60;/data/{index}/attributes/bearing&#x60; | descending | &#x60;-bearing&#x60; | | &#x60;/data/{index}/attributes/current_status&#x60; | ascending | &#x60;current_status&#x60; | | &#x60;/data/{index}/attributes/current_status&#x60; | descending | &#x60;-current_status&#x60; | | &#x60;/data/{index}/attributes/current_stop_sequence&#x60; | ascending | &#x60;current_stop_sequence&#x60; | | &#x60;/data/{index}/attributes/current_stop_sequence&#x60; | descending | &#x60;-current_stop_sequence&#x60; | | &#x60;/data/{index}/attributes/direction_id&#x60; | ascending | &#x60;direction_id&#x60; | | &#x60;/data/{index}/attributes/direction_id&#x60; | descending | &#x60;-direction_id&#x60; | | &#x60;/data/{index}/attributes/label&#x60; | ascending | &#x60;label&#x60; | | &#x60;/data/{index}/attributes/label&#x60; | descending | &#x60;-label&#x60; | | &#x60;/data/{index}/attributes/last_updated&#x60; | ascending | &#x60;last_updated&#x60; | | &#x60;/data/{index}/attributes/last_updated&#x60; | descending | &#x60;-last_updated&#x60; | | &#x60;/data/{index}/attributes/latitude&#x60; | ascending | &#x60;latitude&#x60; | | &#x60;/data/{index}/attributes/latitude&#x60; | descending | &#x60;-latitude&#x60; | | &#x60;/data/{index}/attributes/longitude&#x60; | ascending | &#x60;longitude&#x60; | | &#x60;/data/{index}/attributes/longitude&#x60; | descending | &#x60;-longitude&#x60; | | &#x60;/data/{index}/attributes/speed&#x60; | ascending | &#x60;speed&#x60; | | &#x60;/data/{index}/attributes/speed&#x60; | descending | &#x60;-speed&#x60; |   | [optional] 
 **api_key** | **str**| Key for API access.  Without api_key, requests will be tracked by IP address and have stricter rate limit. [Register for a key](/register)  | [optional] 
 **include** | **str**| Relationships to include.  * &#x60;trip&#x60; * &#x60;stop&#x60; * &#x60;route&#x60;  The value of the include parameter **MUST** be a comma-separated (U+002C COMMA, \&quot;,\&quot;) list of relationship paths. A relationship path is a dot-separated (U+002E FULL-STOP, \&quot;.\&quot;) list of relationship names. [JSONAPI \&quot;include\&quot; behavior](http://jsonapi.org/format/#fetching-includes)  | include | Description                                                                                                                                                                                                                                                                                                                                                  | |---------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| | &#x60;trip&#x60;  | The trip which the vehicle is currently operating.                                                                                                                                                                                                                                                                                                           | | &#x60;stop&#x60;  | The vehicle&#39;s current (when &#x60;current_status&#x60; is **STOPPED_AT**) or *next* stop.                                                                                                                                                                                                                                                                              | | &#x60;route&#x60; | The one route that is designated for that trip, as in GTFS &#x60;trips.txt&#x60;.  A trip might also provide service on other routes, identified by the MBTA&#39;s &#x60;multi_route_trips.txt&#x60; GTFS extension. &#x60;filter[route]&#x60; does consider the multi_route_trips GTFS extension, so it is possible to filter for one route and get a different route included in the response. |   | [optional] 
 **filter_trip** | **str**| Filter by &#x60;/data/{index}/relationships/trip/data/id&#x60;. Multiple &#x60;/data/{index}/relationships/trip/data/id&#x60; **MUST** be a comma-separated (U+002C COMMA, \&quot;,\&quot;) list. | [optional] 
 **filter_route** | **str**| Filter by route. If the vehicle is on a [multi-route trip](https://groups.google.com/forum/#!msg/massdotdevelopers/1egrhNjT9eA/iy6NFymcCgAJ), it will be returned for any of the routes. Multiple &#x60;route_id&#x60; **MUST** be a comma-separated (U+002C COMMA, \&quot;,\&quot;) list.  | [optional] 
 **filter_direction_id** | **str**| Filter by direction of travel along the route.  The meaning of &#x60;direction_id&#x60; varies based on the route. You can programmatically get the direction names from &#x60;/routes&#x60; &#x60;/data/{index}/attributes/direction_names&#x60; or &#x60;/routes/{id}&#x60; &#x60;/data/attributes/direction_names&#x60;.     | [optional] 

### Return type

[**Vehicles**](Vehicles.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_web_vehicle_controller_show**
> Vehicle api_web_vehicle_controller_show(id, api_key=api_key, include=include)



Single vehicle (bus, ferry, or train)  ## Direction  ### World  To figure out which way the vehicle is pointing at the location, use `/data/attributes/bearing`.  This can be the compass bearing, or the direction towards the next stop or intermediate location.  ### Trip  To get the direction around the stops in the trip use `/data/attributes/direction_id`.  ## Location  ### World  Use `/data/attributes/latitude` and `/data/attributes/longitude` to get the location of a vehicle.  ### Trip  Use `/data/attributes/current_stop_sequence` to get the stop number along the trip.  Useful for linear stop indicators.  Position relative to the current stop is in `/data/attributes/current_status`.  ## Movement  ### World  Use `/data/attributes/speed` to get the speed of the vehicle in meters per second.  

### Example 
```python
from __future__ import print_function
import time
import mbtaapi
from mbtaapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mbtaapi.VehicleApi()
id = 'id_example' # str | Unique identifier for a vehicle
api_key = 'api_key_example' # str | Key for API access.  Without api_key, requests will be tracked by IP address and have stricter rate limit. [Register for a key](/register)  (optional)
include = 'include_example' # str | Relationships to include.  * `trip` * `stop` * `route`  The value of the include parameter **MUST** be a comma-separated (U+002C COMMA, \",\") list of relationship paths. A relationship path is a dot-separated (U+002E FULL-STOP, \".\") list of relationship names. [JSONAPI \"include\" behavior](http://jsonapi.org/format/#fetching-includes)  | include | Description                                                                                                                                                                                                                                                                                                                                                  | |---------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| | `trip`  | The trip which the vehicle is currently operating.                                                                                                                                                                                                                                                                                                           | | `stop`  | The vehicle's current (when `current_status` is **STOPPED_AT**) or *next* stop.                                                                                                                                                                                                                                                                              | | `route` | The one route that is designated for that trip, as in GTFS `trips.txt`.  A trip might also provide service on other routes, identified by the MBTA's `multi_route_trips.txt` GTFS extension. `filter[route]` does consider the multi_route_trips GTFS extension, so it is possible to filter for one route and get a different route included in the response. |   (optional)

try: 
    # 
    api_response = api_instance.api_web_vehicle_controller_show(id, api_key=api_key, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VehicleApi->api_web_vehicle_controller_show: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier for a vehicle | 
 **api_key** | **str**| Key for API access.  Without api_key, requests will be tracked by IP address and have stricter rate limit. [Register for a key](/register)  | [optional] 
 **include** | **str**| Relationships to include.  * &#x60;trip&#x60; * &#x60;stop&#x60; * &#x60;route&#x60;  The value of the include parameter **MUST** be a comma-separated (U+002C COMMA, \&quot;,\&quot;) list of relationship paths. A relationship path is a dot-separated (U+002E FULL-STOP, \&quot;.\&quot;) list of relationship names. [JSONAPI \&quot;include\&quot; behavior](http://jsonapi.org/format/#fetching-includes)  | include | Description                                                                                                                                                                                                                                                                                                                                                  | |---------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| | &#x60;trip&#x60;  | The trip which the vehicle is currently operating.                                                                                                                                                                                                                                                                                                           | | &#x60;stop&#x60;  | The vehicle&#39;s current (when &#x60;current_status&#x60; is **STOPPED_AT**) or *next* stop.                                                                                                                                                                                                                                                                              | | &#x60;route&#x60; | The one route that is designated for that trip, as in GTFS &#x60;trips.txt&#x60;.  A trip might also provide service on other routes, identified by the MBTA&#39;s &#x60;multi_route_trips.txt&#x60; GTFS extension. &#x60;filter[route]&#x60; does consider the multi_route_trips GTFS extension, so it is possible to filter for one route and get a different route included in the response. |   | [optional] 

### Return type

[**Vehicle**](Vehicle.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

