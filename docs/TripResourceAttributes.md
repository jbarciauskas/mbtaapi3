# TripResourceAttributes

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**wheelchair_accessible** | **int** | Indicator of wheelchair accessibility: &#x60;0&#x60;, &#x60;1&#x60;, &#x60;2&#x60;  Wheelchair accessibility (&#x60;*/attributes/wheelchair_accessible&#x60;) [as defined in GTFS](https://github.com/google/transit/blob/master/gtfs/spec/en/reference.md#tripstxt):  | Value | Meaning                                            | |-------|----------------------------------------------------| | &#x60;0&#x60;   | No information                                     | | &#x60;1&#x60;   | Accessible (at stops allowing wheelchair_boarding) | | &#x60;2&#x60;   | Inaccessible                                       |   | [optional] 
**name** | **str** | The text that appears in schedules and sign boards to identify the trip to passengers, for example, to identify train numbers for commuter rail trips. See [GTFS &#x60;trips.txt&#x60; &#x60;trip_short_name&#x60;](https://github.com/google/transit/blob/master/gtfs/spec/en/reference.md#tripstxt)  | [optional] 
**headsign** | **str** | The text that appears on a sign that identifies the trip&#39;s destination to passengers. See [GTFS &#x60;trips.txt&#x60; &#x60;trip_headsign&#x60;](https://github.com/google/transit/blob/master/gtfs/spec/en/reference.md#tripstxt).  | [optional] 
**direction_id** | **int** | Direction in which trip is traveling: &#x60;0&#x60; or &#x60;1&#x60;.  The meaning of &#x60;direction_id&#x60; varies based on the route. You can programmatically get the direction names from &#x60;/routes&#x60; &#x60;/data/{index}/attributes/direction_names&#x60; or &#x60;/routes/{id}&#x60; &#x60;/data/attributes/direction_names&#x60;.   | [optional] 
**block_id** | **str** | ID used to group sequential trips with the same vehicle for a given service_id. See [GTFS &#x60;trips.txt&#x60; &#x60;block_id&#x60;](https://github.com/google/transit/blob/master/gtfs/spec/en/reference.md#tripstxt)  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


