# StopResourceAttributes

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**wheelchair_boarding** | **int** | Whether there are any vehicles with wheelchair boarding or paths to stops that are wheelchair acessible: 0, 1, 2.  Wheelchair boarding (&#x60;*/attributes/wheelchair_boarding&#x60;) corresponds to [GTFS wheelchair_boarding](https://github.com/google/transit/blob/master/gtfs/spec/en/reference.md#stopstxt). The MBTA handles parent station inheritance itself, so value can be treated simply:  | Value | Meaning                                       | |-------|-----------------------------------------------| | &#x60;0&#x60;   | No Information                                | | &#x60;1&#x60;   | Accessible (if trip is wheelchair accessible) | | &#x60;2&#x60;   | Inaccessible                                  |   | [optional] 
**name** | **str** | Name of a stop or station in the local and tourist vernacular.  See [GTFS &#x60;stops.txt&#x60; &#x60;stop_name](https://github.com/google/transit/blob/master/gtfs/spec/en/reference.md#stopstxt)  | [optional] 
**longitude** | **float** | Longitude of the stop or station. Degrees East, in the [WGS-84](https://en.wikipedia.org/wiki/World_Geodetic_System#Longitudes_on_WGS.C2.A084) coordinate system. See [GTFS &#x60;stops.txt&#x60; &#x60;stop_lon&#x60;](https://github.com/google/transit/blob/master/gtfs/spec/en/reference.md#stopstxt).  | [optional] 
**latitude** | **float** | Latitude of the stop or station.  Degrees North, in the [WGS-84](https://en.wikipedia.org/wiki/World_Geodetic_System#A_new_World_Geodetic_System:_WGS.C2.A084) coordinate system. See [GTFS &#x60;stops.txt&#x60; &#x60;stop_lat&#x60;](https://github.com/google/transit/blob/master/gtfs/spec/en/reference.md#stopstxt).  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


