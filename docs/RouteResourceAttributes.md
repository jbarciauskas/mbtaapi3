# RouteResourceAttributes

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **int** | | Value | Name          | Example    | |-------|---------------|------------| | &#x60;0&#x60;   | Light Rail    | Green Line | | &#x60;1&#x60;   | Heavy Rail    | Red Line   | | &#x60;2&#x60;   | Commuter Rail |            | | &#x60;3&#x60;   | Bus           |            | | &#x60;4&#x60;   | Ferry         |            |  | [optional] 
**sort_order** | **int** | Routes sort in ascending order | [optional] 
**short_name** | **str** | This will often be a short, abstract identifier like \&quot;32\&quot;, \&quot;100X\&quot;, or \&quot;Green\&quot; that riders use to identify a route, but which doesn&#39;t give any indication of what places the route serves. See [GTFS &#x60;routes.txt&#x60; &#x60;route_short_name&#x60;](https://github.com/google/transit/blob/master/gtfs/spec/en/reference.md#routestxt).  | [optional] 
**long_name** | **str** | The full name of a route. This name is generally more descriptive than the &#x60;short_name&#x60; and will often include the route&#39;s destination or stop. See [GTFS &#x60;routes.txt&#x60; &#x60;route_long_name&#x60;](https://github.com/google/transit/blob/master/gtfs/spec/en/reference.md#routestxt).  | [optional] 
**direction_names** | **list[str]** |  | [optional] 
**description** | **str** | Details about stops, schedule, and/or service.  See [GTFS &#x60;routes.txt&#x60; &#x60;route_desc&#x60;](https://github.com/google/transit/blob/master/gtfs/spec/en/reference.md#routestxt).  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


