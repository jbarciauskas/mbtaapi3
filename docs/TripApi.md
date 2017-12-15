# mbtaapi.TripApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_web_trip_controller_index**](TripApi.md#api_web_trip_controller_index) | **GET** /trips | 
[**api_web_trip_controller_show**](TripApi.md#api_web_trip_controller_show) | **GET** /trips/{id} | 


# **api_web_trip_controller_index**
> Trips api_web_trip_controller_index(page_offset=page_offset, page_limit=page_limit, sort=sort, api_key=api_key, include=include, filter_date=filter_date, filter_direction_id=filter_direction_id, filter_route=filter_route)



**NOTE:** A filter **MUST** be present for any trips to be returned.  List of trips, the journies of a particular vehicle through a set of stops on a primary `route` and zero or more alternative `route`s that can be filtered on.  ## Accessibility  Wheelchair accessibility (`/data/{index}/attributes/wheelchair_accessible`) [as defined in GTFS](https://github.com/google/transit/blob/master/gtfs/spec/en/reference.md#tripstxt):  | Value | Meaning                                            | |-------|----------------------------------------------------| | `0`   | No information                                     | | `1`   | Accessible (at stops allowing wheelchair_boarding) | | `2`   | Inaccessible                                       |   ## Grouping  Multiple trips **may** be grouped together using `/data/{index}/attributes/block_id`. A block represents a series of trips scheduled to be operated by the same vehicle.  ## Naming  There are 3 names associated with a trip.  | API Field                   | GTFS              | Show users? | |-----------------------------|-------------------|-------------| | `/data/attributes/headsign` | `trip_headsign`   | Yes         | | `/data/attributes/name`     | `trip_short_name` | Yes         | | `/data/id`                  | `trip_id`         | No          |   

### Example 
```python
from __future__ import print_function
import time
import mbtaapi
from mbtaapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mbtaapi.TripApi()
page_offset = 56 # int | Offset (0-based) of first element in the page (optional)
page_limit = 56 # int | Max number of elements to return (optional)
sort = 'sort_example' # str | Results can be [sorted](http://jsonapi.org/format/#fetching-sorting) by the id or any `/data/{index}/attributes` key. Assumes ascending; may be prefixed with '-' for descending  | JSON pointer | Direction | `sort`     | |--------------|-----------|------------| | `/data/{index}/attributes/block_id` | ascending | `block_id` | | `/data/{index}/attributes/block_id` | descending | `-block_id` | | `/data/{index}/attributes/direction_id` | ascending | `direction_id` | | `/data/{index}/attributes/direction_id` | descending | `-direction_id` | | `/data/{index}/attributes/headsign` | ascending | `headsign` | | `/data/{index}/attributes/headsign` | descending | `-headsign` | | `/data/{index}/attributes/name` | ascending | `name` | | `/data/{index}/attributes/name` | descending | `-name` | | `/data/{index}/attributes/wheelchair_accessible` | ascending | `wheelchair_accessible` | | `/data/{index}/attributes/wheelchair_accessible` | descending | `-wheelchair_accessible` |   (optional)
api_key = 'api_key_example' # str | Key for API access.  Without api_key, requests will be tracked by IP address and have stricter rate limit. [Register for a key](/register)  (optional)
include = 'include_example' # str | Relationships to include.  * `route` * `vehicle` * `service` * `predictions`  The value of the include parameter **MUST** be a comma-separated (U+002C COMMA, \",\") list of relationship paths. A relationship path is a dot-separated (U+002E FULL-STOP, \".\") list of relationship names. [JSONAPI \"include\" behavior](http://jsonapi.org/format/#fetching-includes)  | include       | Description | |---------------|-------------| | `route`       | The *primary* route for the trip. | | `vehicle`     | The vehicle on this trip. | | `service`     | The service controlling when this trip is active. | | `predictions` | Predictions of when the `vehicle` on this `trip` will arrive at or depart from each stop on the route(s) on the `trip`. |   (optional)
filter_date = '2013-10-20' # date | Filter by trips on a particular date YYYY-MM-DD (optional)
filter_direction_id = 'filter_direction_id_example' # str | Filter by direction of travel along the route.  The meaning of `direction_id` varies based on the route. You can programmatically get the direction names from `/routes` `/data/{index}/attributes/direction_names` or `/routes/{id}` `/data/attributes/direction_names`.     (optional)
filter_route = 'filter_route_example' # str | Filter by `/data/{index}/relationships/route/data/id`. Required (optional)

try: 
    # 
    api_response = api_instance.api_web_trip_controller_index(page_offset=page_offset, page_limit=page_limit, sort=sort, api_key=api_key, include=include, filter_date=filter_date, filter_direction_id=filter_direction_id, filter_route=filter_route)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TripApi->api_web_trip_controller_index: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_offset** | **int**| Offset (0-based) of first element in the page | [optional] 
 **page_limit** | **int**| Max number of elements to return | [optional] 
 **sort** | **str**| Results can be [sorted](http://jsonapi.org/format/#fetching-sorting) by the id or any &#x60;/data/{index}/attributes&#x60; key. Assumes ascending; may be prefixed with &#39;-&#39; for descending  | JSON pointer | Direction | &#x60;sort&#x60;     | |--------------|-----------|------------| | &#x60;/data/{index}/attributes/block_id&#x60; | ascending | &#x60;block_id&#x60; | | &#x60;/data/{index}/attributes/block_id&#x60; | descending | &#x60;-block_id&#x60; | | &#x60;/data/{index}/attributes/direction_id&#x60; | ascending | &#x60;direction_id&#x60; | | &#x60;/data/{index}/attributes/direction_id&#x60; | descending | &#x60;-direction_id&#x60; | | &#x60;/data/{index}/attributes/headsign&#x60; | ascending | &#x60;headsign&#x60; | | &#x60;/data/{index}/attributes/headsign&#x60; | descending | &#x60;-headsign&#x60; | | &#x60;/data/{index}/attributes/name&#x60; | ascending | &#x60;name&#x60; | | &#x60;/data/{index}/attributes/name&#x60; | descending | &#x60;-name&#x60; | | &#x60;/data/{index}/attributes/wheelchair_accessible&#x60; | ascending | &#x60;wheelchair_accessible&#x60; | | &#x60;/data/{index}/attributes/wheelchair_accessible&#x60; | descending | &#x60;-wheelchair_accessible&#x60; |   | [optional] 
 **api_key** | **str**| Key for API access.  Without api_key, requests will be tracked by IP address and have stricter rate limit. [Register for a key](/register)  | [optional] 
 **include** | **str**| Relationships to include.  * &#x60;route&#x60; * &#x60;vehicle&#x60; * &#x60;service&#x60; * &#x60;predictions&#x60;  The value of the include parameter **MUST** be a comma-separated (U+002C COMMA, \&quot;,\&quot;) list of relationship paths. A relationship path is a dot-separated (U+002E FULL-STOP, \&quot;.\&quot;) list of relationship names. [JSONAPI \&quot;include\&quot; behavior](http://jsonapi.org/format/#fetching-includes)  | include       | Description | |---------------|-------------| | &#x60;route&#x60;       | The *primary* route for the trip. | | &#x60;vehicle&#x60;     | The vehicle on this trip. | | &#x60;service&#x60;     | The service controlling when this trip is active. | | &#x60;predictions&#x60; | Predictions of when the &#x60;vehicle&#x60; on this &#x60;trip&#x60; will arrive at or depart from each stop on the route(s) on the &#x60;trip&#x60;. |   | [optional] 
 **filter_date** | **date**| Filter by trips on a particular date YYYY-MM-DD | [optional] 
 **filter_direction_id** | **str**| Filter by direction of travel along the route.  The meaning of &#x60;direction_id&#x60; varies based on the route. You can programmatically get the direction names from &#x60;/routes&#x60; &#x60;/data/{index}/attributes/direction_names&#x60; or &#x60;/routes/{id}&#x60; &#x60;/data/attributes/direction_names&#x60;.     | [optional] 
 **filter_route** | **str**| Filter by &#x60;/data/{index}/relationships/route/data/id&#x60;. Required | [optional] 

### Return type

[**Trips**](Trips.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_web_trip_controller_show**
> Trip api_web_trip_controller_show(id, api_key=api_key, include=include)



Single trip - the journey of a particular vehicle through a set of stops  ## Accessibility  Wheelchair accessibility (`/data/attributes/wheelchair_accessible`) [as defined in GTFS](https://github.com/google/transit/blob/master/gtfs/spec/en/reference.md#tripstxt):  | Value | Meaning                                            | |-------|----------------------------------------------------| | `0`   | No information                                     | | `1`   | Accessible (at stops allowing wheelchair_boarding) | | `2`   | Inaccessible                                       |   ## Grouping  Multiple trips **may** be grouped together using `/data/attributes/block_id`. A block represents a series of trips scheduled to be operated by the same vehicle.  ## Naming  There are 3 names associated with a trip.  | API Field                   | GTFS              | Show users? | |-----------------------------|-------------------|-------------| | `/data/attributes/headsign` | `trip_headsign`   | Yes         | | `/data/attributes/name`     | `trip_short_name` | Yes         | | `/data/id`                  | `trip_id`         | No          |   

### Example 
```python
from __future__ import print_function
import time
import mbtaapi
from mbtaapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mbtaapi.TripApi()
id = 'id_example' # str | Unique identifier for a trip
api_key = 'api_key_example' # str | Key for API access.  Without api_key, requests will be tracked by IP address and have stricter rate limit. [Register for a key](/register)  (optional)
include = 'include_example' # str | Relationships to include.  * `route` * `vehicle` * `service` * `predictions`  The value of the include parameter **MUST** be a comma-separated (U+002C COMMA, \",\") list of relationship paths. A relationship path is a dot-separated (U+002E FULL-STOP, \".\") list of relationship names. [JSONAPI \"include\" behavior](http://jsonapi.org/format/#fetching-includes)  | include       | Description | |---------------|-------------| | `route`       | The *primary* route for the trip. | | `vehicle`     | The vehicle on this trip. | | `service`     | The service controlling when this trip is active. | | `predictions` | Predictions of when the `vehicle` on this `trip` will arrive at or depart from each stop on the route(s) on the `trip`. |   (optional)

try: 
    # 
    api_response = api_instance.api_web_trip_controller_show(id, api_key=api_key, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TripApi->api_web_trip_controller_show: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier for a trip | 
 **api_key** | **str**| Key for API access.  Without api_key, requests will be tracked by IP address and have stricter rate limit. [Register for a key](/register)  | [optional] 
 **include** | **str**| Relationships to include.  * &#x60;route&#x60; * &#x60;vehicle&#x60; * &#x60;service&#x60; * &#x60;predictions&#x60;  The value of the include parameter **MUST** be a comma-separated (U+002C COMMA, \&quot;,\&quot;) list of relationship paths. A relationship path is a dot-separated (U+002E FULL-STOP, \&quot;.\&quot;) list of relationship names. [JSONAPI \&quot;include\&quot; behavior](http://jsonapi.org/format/#fetching-includes)  | include       | Description | |---------------|-------------| | &#x60;route&#x60;       | The *primary* route for the trip. | | &#x60;vehicle&#x60;     | The vehicle on this trip. | | &#x60;service&#x60;     | The service controlling when this trip is active. | | &#x60;predictions&#x60; | Predictions of when the &#x60;vehicle&#x60; on this &#x60;trip&#x60; will arrive at or depart from each stop on the route(s) on the &#x60;trip&#x60;. |   | [optional] 

### Return type

[**Trip**](Trip.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

