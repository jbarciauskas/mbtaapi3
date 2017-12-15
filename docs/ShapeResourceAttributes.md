# ShapeResourceAttributes

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**priority** | **int** | Representation of how important a shape is when choosing one for display. Higher number is higher priority.  Negative priority is not important enough to show as they only **MAY** be used.  | [optional] 
**polyline** | **str** | ## Encoding/Decoding  [Encoded Polyline Algorithm Format](https://developers.google.com/maps/documentation/utilities/polylinealgorithm)  ## Example Libraries  * [Javascript](https://www.npmjs.com/package/polyline) * [Erlang](https://blog.kempkens.io/posts/encoding-and-decoding-polylines-with-erlang/) * [Elixir](https://hex.pm/packages/polyline)  | [optional] 
**name** | **str** | User-facing name for shape. It may, but is not required to, be a headsign | [optional] 
**direction_id** | **int** | Direction in which trip is traveling: &#x60;0&#x60; or &#x60;1&#x60;.  The meaning of &#x60;direction_id&#x60; varies based on the route. You can programmatically get the direction names from &#x60;/routes&#x60; &#x60;/data/{index}/attributes/direction_names&#x60; or &#x60;/routes/{id}&#x60; &#x60;/data/attributes/direction_names&#x60;.   | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


