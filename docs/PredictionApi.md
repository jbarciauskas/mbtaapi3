# mbtaapi.PredictionApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_web_prediction_controller_index**](PredictionApi.md#api_web_prediction_controller_index) | **GET** /predictions | 


# **api_web_prediction_controller_index**
> Predictions api_web_prediction_controller_index(page_offset=page_offset, page_limit=page_limit, sort=sort, api_key=api_key, include=include, filter_latitude=filter_latitude, filter_longitude=filter_longitude, filter_direction_id=filter_direction_id, filter_stop=filter_stop, filter_route=filter_route, filter_trip=filter_trip)



**NOTE:** A filter **MUST** be present for any predictions to be returned.  List of predictions for trips.  To get the scheduled times instead of the predictions, use `/schedules`.  The predicted arrival time (`//data/{index}/attributes/arrival_time`) and departure time (`/data/{index}/attributes/departure_time`) to/from a stop (`/data/{index}/relationships/stop/data/id`) at a given sequence (`/data/{index}/attriutes/stop_sequence`) along a trip (`/data/{index}/relationships/trip/data/id`) going a direction (`/data/{index}/attributes/direction_id`) along a route (`/data/{index}/relationships/route/data/id`).  See [GTFS Realtime `FeedMesage` `FeedEntity` `TripUpdate` `TripDescriptor`](https://github.com/google/transit/blob/master/gtfs-realtime/spec/en/reference.md#message-tripdescriptor) See [GTFS Realtime `FeedMesage` `FeedEntity` `TripUpdate` `StopTimeUpdate`](https://github.com/google/transit/blob/master/gtfs-realtime/spec/en/reference.md#message-stoptimeupdate)   ## When a vehicle is predicted to be at a stop  `/predictions?filter[stop]=STOP_ID`  ## The predicted schedule for one route  `/predictions?filter[route]=ROUTE_ID`  ## The predicted schedule for a whole trip  `/predictions?filter[trip]=TRIP_ID`  

### Example 
```python
from __future__ import print_function
import time
import mbtaapi
from mbtaapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mbtaapi.PredictionApi()
page_offset = 56 # int | Offset (0-based) of first element in the page (optional)
page_limit = 56 # int | Max number of elements to return (optional)
sort = 'sort_example' # str | Results can be [sorted](http://jsonapi.org/format/#fetching-sorting) by the id or any `/data/{index}/attributes` key. Assumes ascending; may be prefixed with '-' for descending  | JSON pointer | Direction | `sort`     | |--------------|-----------|------------| | `/data/{index}/attributes/arrival_time` | ascending | `arrival_time` | | `/data/{index}/attributes/arrival_time` | descending | `-arrival_time` | | `/data/{index}/attributes/departure_time` | ascending | `departure_time` | | `/data/{index}/attributes/departure_time` | descending | `-departure_time` | | `/data/{index}/attributes/direction_id` | ascending | `direction_id` | | `/data/{index}/attributes/direction_id` | descending | `-direction_id` | | `/data/{index}/attributes/schedule_relationship` | ascending | `schedule_relationship` | | `/data/{index}/attributes/schedule_relationship` | descending | `-schedule_relationship` | | `/data/{index}/attributes/status` | ascending | `status` | | `/data/{index}/attributes/status` | descending | `-status` | | `/data/{index}/attributes/stop_sequence` | ascending | `stop_sequence` | | `/data/{index}/attributes/stop_sequence` | descending | `-stop_sequence` | | `/data/{index}/attributes/track` | ascending | `track` | | `/data/{index}/attributes/track` | descending | `-track` |   (optional)
api_key = 'api_key_example' # str | Key for API access.  Without api_key, requests will be tracked by IP address and have stricter rate limit. [Register for a key](/register)  (optional)
include = 'include_example' # str | Relationships to include.  * `schedule` * `stop` * `route` * `trip` * `vehicle` * `alerts`  The value of the include parameter **MUST** be a comma-separated (U+002C COMMA, \",\") list of relationship paths. A relationship path is a dot-separated (U+002E FULL-STOP, \".\") list of relationship names. [JSONAPI \"include\" behavior](http://jsonapi.org/format/#fetching-includes)    (optional)
filter_latitude = 'filter_latitude_example' # str |  Latitude/Longitude must be both present or both absent. (optional)
filter_longitude = 'filter_longitude_example' # str |  Latitude/Longitude must be both present or both absent. (optional)
filter_direction_id = 'filter_direction_id_example' # str | Filter by direction of travel along the route.  The meaning of `direction_id` varies based on the route. You can programmatically get the direction names from `/routes` `/data/{index}/attributes/direction_names` or `/routes/{id}` `/data/attributes/direction_names`.     (optional)
filter_stop = 'filter_stop_example' # str | Filter by `/data/{index}/relationships/stop/data/id`. Multiple `/data/{index}/relationships/stop/data/id` **MUST** be a comma-separated (U+002C COMMA, \",\") list. (optional)
filter_route = 'filter_route_example' # str | Filter by `/data/{index}/relationships/route/data/id`. Multiple `/data/{index}/relationships/route/data/id` **MUST** be a comma-separated (U+002C COMMA, \",\") list. (optional)
filter_trip = 'filter_trip_example' # str | Filter by `/data/{index}/relationships/trip/data/id`. Multiple `/data/{index}/relationships/trip/data/id` **MUST** be a comma-separated (U+002C COMMA, \",\") list. (optional)

try: 
    # 
    api_response = api_instance.api_web_prediction_controller_index(page_offset=page_offset, page_limit=page_limit, sort=sort, api_key=api_key, include=include, filter_latitude=filter_latitude, filter_longitude=filter_longitude, filter_direction_id=filter_direction_id, filter_stop=filter_stop, filter_route=filter_route, filter_trip=filter_trip)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PredictionApi->api_web_prediction_controller_index: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_offset** | **int**| Offset (0-based) of first element in the page | [optional] 
 **page_limit** | **int**| Max number of elements to return | [optional] 
 **sort** | **str**| Results can be [sorted](http://jsonapi.org/format/#fetching-sorting) by the id or any &#x60;/data/{index}/attributes&#x60; key. Assumes ascending; may be prefixed with &#39;-&#39; for descending  | JSON pointer | Direction | &#x60;sort&#x60;     | |--------------|-----------|------------| | &#x60;/data/{index}/attributes/arrival_time&#x60; | ascending | &#x60;arrival_time&#x60; | | &#x60;/data/{index}/attributes/arrival_time&#x60; | descending | &#x60;-arrival_time&#x60; | | &#x60;/data/{index}/attributes/departure_time&#x60; | ascending | &#x60;departure_time&#x60; | | &#x60;/data/{index}/attributes/departure_time&#x60; | descending | &#x60;-departure_time&#x60; | | &#x60;/data/{index}/attributes/direction_id&#x60; | ascending | &#x60;direction_id&#x60; | | &#x60;/data/{index}/attributes/direction_id&#x60; | descending | &#x60;-direction_id&#x60; | | &#x60;/data/{index}/attributes/schedule_relationship&#x60; | ascending | &#x60;schedule_relationship&#x60; | | &#x60;/data/{index}/attributes/schedule_relationship&#x60; | descending | &#x60;-schedule_relationship&#x60; | | &#x60;/data/{index}/attributes/status&#x60; | ascending | &#x60;status&#x60; | | &#x60;/data/{index}/attributes/status&#x60; | descending | &#x60;-status&#x60; | | &#x60;/data/{index}/attributes/stop_sequence&#x60; | ascending | &#x60;stop_sequence&#x60; | | &#x60;/data/{index}/attributes/stop_sequence&#x60; | descending | &#x60;-stop_sequence&#x60; | | &#x60;/data/{index}/attributes/track&#x60; | ascending | &#x60;track&#x60; | | &#x60;/data/{index}/attributes/track&#x60; | descending | &#x60;-track&#x60; |   | [optional] 
 **api_key** | **str**| Key for API access.  Without api_key, requests will be tracked by IP address and have stricter rate limit. [Register for a key](/register)  | [optional] 
 **include** | **str**| Relationships to include.  * &#x60;schedule&#x60; * &#x60;stop&#x60; * &#x60;route&#x60; * &#x60;trip&#x60; * &#x60;vehicle&#x60; * &#x60;alerts&#x60;  The value of the include parameter **MUST** be a comma-separated (U+002C COMMA, \&quot;,\&quot;) list of relationship paths. A relationship path is a dot-separated (U+002E FULL-STOP, \&quot;.\&quot;) list of relationship names. [JSONAPI \&quot;include\&quot; behavior](http://jsonapi.org/format/#fetching-includes)    | [optional] 
 **filter_latitude** | **str**|  Latitude/Longitude must be both present or both absent. | [optional] 
 **filter_longitude** | **str**|  Latitude/Longitude must be both present or both absent. | [optional] 
 **filter_direction_id** | **str**| Filter by direction of travel along the route.  The meaning of &#x60;direction_id&#x60; varies based on the route. You can programmatically get the direction names from &#x60;/routes&#x60; &#x60;/data/{index}/attributes/direction_names&#x60; or &#x60;/routes/{id}&#x60; &#x60;/data/attributes/direction_names&#x60;.     | [optional] 
 **filter_stop** | **str**| Filter by &#x60;/data/{index}/relationships/stop/data/id&#x60;. Multiple &#x60;/data/{index}/relationships/stop/data/id&#x60; **MUST** be a comma-separated (U+002C COMMA, \&quot;,\&quot;) list. | [optional] 
 **filter_route** | **str**| Filter by &#x60;/data/{index}/relationships/route/data/id&#x60;. Multiple &#x60;/data/{index}/relationships/route/data/id&#x60; **MUST** be a comma-separated (U+002C COMMA, \&quot;,\&quot;) list. | [optional] 
 **filter_trip** | **str**| Filter by &#x60;/data/{index}/relationships/trip/data/id&#x60;. Multiple &#x60;/data/{index}/relationships/trip/data/id&#x60; **MUST** be a comma-separated (U+002C COMMA, \&quot;,\&quot;) list. | [optional] 

### Return type

[**Predictions**](Predictions.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

