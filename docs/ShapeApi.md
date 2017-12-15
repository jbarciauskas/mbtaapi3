# mbtaapi.ShapeApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_web_shape_controller_index**](ShapeApi.md#api_web_shape_controller_index) | **GET** /shapes | 
[**api_web_shape_controller_show**](ShapeApi.md#api_web_shape_controller_show) | **GET** /shapes/{id} | 


# **api_web_shape_controller_index**
> Shapes api_web_shape_controller_index(filter_route, page_offset=page_offset, page_limit=page_limit, sort=sort, api_key=api_key, include=include, filter_direction_id=filter_direction_id)



**NOTE:** `filter[route]` **MUST** be given for any shapes to be returned.  List of shapes.  ## Vertices  ### World  `/data/{index}/attributes/polyline` is in [Encoded Polyline Algorithm Format](https://developers.google.com/maps/documentation/utilities/polylinealgorithm), which encodes the latitude and longitude of a sequence of points in the shape.  ### Stops  If instead of getting the latitude and longitude directly, you want to show the stops in this shape use `/data/{index}/relationships/stops` to get the all the stop IDs or `include=stops` to include them in the response.  

### Example 
```python
from __future__ import print_function
import time
import mbtaapi
from mbtaapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mbtaapi.ShapeApi()
filter_route = 'filter_route_example' # str | Filter by `/data/{index}/relationships/route/data/id`. Multiple `/data/{index}/relationships/route/data/id` **MUST** be a comma-separated (U+002C COMMA, \",\") list.
page_offset = 56 # int | Offset (0-based) of first element in the page (optional)
page_limit = 56 # int | Max number of elements to return (optional)
sort = 'sort_example' # str | Results can be [sorted](http://jsonapi.org/format/#fetching-sorting) by the id or any `/data/{index}/attributes` key. Assumes ascending; may be prefixed with '-' for descending  | JSON pointer | Direction | `sort`     | |--------------|-----------|------------| | `/data/{index}/attributes/direction_id` | ascending | `direction_id` | | `/data/{index}/attributes/direction_id` | descending | `-direction_id` | | `/data/{index}/attributes/name` | ascending | `name` | | `/data/{index}/attributes/name` | descending | `-name` | | `/data/{index}/attributes/polyline` | ascending | `polyline` | | `/data/{index}/attributes/polyline` | descending | `-polyline` | | `/data/{index}/attributes/priority` | ascending | `priority` | | `/data/{index}/attributes/priority` | descending | `-priority` |   (optional)
api_key = 'api_key_example' # str | Key for API access.  Without api_key, requests will be tracked by IP address and have stricter rate limit. [Register for a key](/register)  (optional)
include = 'include_example' # str | Relationships to include.  * `route` * `stops`  The value of the include parameter **MUST** be a comma-separated (U+002C COMMA, \",\") list of relationship paths. A relationship path is a dot-separated (U+002E FULL-STOP, \".\") list of relationship names. [JSONAPI \"include\" behavior](http://jsonapi.org/format/#fetching-includes)    (optional)
filter_direction_id = 'filter_direction_id_example' # str | Filter by direction of travel along the route.  The meaning of `direction_id` varies based on the route. You can programmatically get the direction names from `/routes` `/data/{index}/attributes/direction_names` or `/routes/{id}` `/data/attributes/direction_names`.     (optional)

try: 
    # 
    api_response = api_instance.api_web_shape_controller_index(filter_route, page_offset=page_offset, page_limit=page_limit, sort=sort, api_key=api_key, include=include, filter_direction_id=filter_direction_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ShapeApi->api_web_shape_controller_index: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_route** | **str**| Filter by &#x60;/data/{index}/relationships/route/data/id&#x60;. Multiple &#x60;/data/{index}/relationships/route/data/id&#x60; **MUST** be a comma-separated (U+002C COMMA, \&quot;,\&quot;) list. | 
 **page_offset** | **int**| Offset (0-based) of first element in the page | [optional] 
 **page_limit** | **int**| Max number of elements to return | [optional] 
 **sort** | **str**| Results can be [sorted](http://jsonapi.org/format/#fetching-sorting) by the id or any &#x60;/data/{index}/attributes&#x60; key. Assumes ascending; may be prefixed with &#39;-&#39; for descending  | JSON pointer | Direction | &#x60;sort&#x60;     | |--------------|-----------|------------| | &#x60;/data/{index}/attributes/direction_id&#x60; | ascending | &#x60;direction_id&#x60; | | &#x60;/data/{index}/attributes/direction_id&#x60; | descending | &#x60;-direction_id&#x60; | | &#x60;/data/{index}/attributes/name&#x60; | ascending | &#x60;name&#x60; | | &#x60;/data/{index}/attributes/name&#x60; | descending | &#x60;-name&#x60; | | &#x60;/data/{index}/attributes/polyline&#x60; | ascending | &#x60;polyline&#x60; | | &#x60;/data/{index}/attributes/polyline&#x60; | descending | &#x60;-polyline&#x60; | | &#x60;/data/{index}/attributes/priority&#x60; | ascending | &#x60;priority&#x60; | | &#x60;/data/{index}/attributes/priority&#x60; | descending | &#x60;-priority&#x60; |   | [optional] 
 **api_key** | **str**| Key for API access.  Without api_key, requests will be tracked by IP address and have stricter rate limit. [Register for a key](/register)  | [optional] 
 **include** | **str**| Relationships to include.  * &#x60;route&#x60; * &#x60;stops&#x60;  The value of the include parameter **MUST** be a comma-separated (U+002C COMMA, \&quot;,\&quot;) list of relationship paths. A relationship path is a dot-separated (U+002E FULL-STOP, \&quot;.\&quot;) list of relationship names. [JSONAPI \&quot;include\&quot; behavior](http://jsonapi.org/format/#fetching-includes)    | [optional] 
 **filter_direction_id** | **str**| Filter by direction of travel along the route.  The meaning of &#x60;direction_id&#x60; varies based on the route. You can programmatically get the direction names from &#x60;/routes&#x60; &#x60;/data/{index}/attributes/direction_names&#x60; or &#x60;/routes/{id}&#x60; &#x60;/data/attributes/direction_names&#x60;.     | [optional] 

### Return type

[**Shapes**](Shapes.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_web_shape_controller_show**
> Shape api_web_shape_controller_show(id, api_key=api_key, include=include)



Detail of a particular shape.  ## Vertices  ### World  `/data/attributes/polyline` is in [Encoded Polyline Algorithm Format](https://developers.google.com/maps/documentation/utilities/polylinealgorithm), which encodes the latitude and longitude of a sequence of points in the shape.  ### Stops  If instead of getting the latitude and longitude directly, you want to show the stops in this shape use `/data/relationships/stops` to get the all the stop IDs or `include=stops` to include them in the response.  

### Example 
```python
from __future__ import print_function
import time
import mbtaapi
from mbtaapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mbtaapi.ShapeApi()
id = 'id_example' # str | Unique identifier for shape
api_key = 'api_key_example' # str | Key for API access.  Without api_key, requests will be tracked by IP address and have stricter rate limit. [Register for a key](/register)  (optional)
include = 'include_example' # str | Relationships to include.  * `route` * `stops`  The value of the include parameter **MUST** be a comma-separated (U+002C COMMA, \",\") list of relationship paths. A relationship path is a dot-separated (U+002E FULL-STOP, \".\") list of relationship names. [JSONAPI \"include\" behavior](http://jsonapi.org/format/#fetching-includes)    (optional)

try: 
    # 
    api_response = api_instance.api_web_shape_controller_show(id, api_key=api_key, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ShapeApi->api_web_shape_controller_show: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier for shape | 
 **api_key** | **str**| Key for API access.  Without api_key, requests will be tracked by IP address and have stricter rate limit. [Register for a key](/register)  | [optional] 
 **include** | **str**| Relationships to include.  * &#x60;route&#x60; * &#x60;stops&#x60;  The value of the include parameter **MUST** be a comma-separated (U+002C COMMA, \&quot;,\&quot;) list of relationship paths. A relationship path is a dot-separated (U+002E FULL-STOP, \&quot;.\&quot;) list of relationship names. [JSONAPI \&quot;include\&quot; behavior](http://jsonapi.org/format/#fetching-includes)    | [optional] 

### Return type

[**Shape**](Shape.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

