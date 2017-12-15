# InformedEntity

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**trip** | **str** | Unique id of a trip | [optional] 
**stop** | **str** | Unique id of a stop | [optional] 
**route_type** | **int** | | Value | Name          | Example    | |-------|---------------|------------| | &#x60;0&#x60;   | Light Rail    | Green Line | | &#x60;1&#x60;   | Heavy Rail    | Red Line   | | &#x60;2&#x60;   | Commuter Rail |            | | &#x60;3&#x60;   | Bus           |            | | &#x60;4&#x60;   | Ferry         |            |  | [optional] 
**route** | **str** | Unique id of a route | [optional] 
**facility** | **str** | Unique id of a facility | [optional] 
**direction_id** | **int** | Direction in which trip is traveling: &#x60;0&#x60; or &#x60;1&#x60;.  The meaning of &#x60;direction_id&#x60; varies based on the route. You can programmatically get the direction names from &#x60;/routes&#x60; &#x60;/data/{index}/attributes/direction_names&#x60; or &#x60;/routes/{id}&#x60; &#x60;/data/attributes/direction_names&#x60;.   | [optional] 
**activities** | [**list[Activity]**](Activity.md) | Activities affected by this alert.  If an entity is a station platform, and the alert only impacts those boarding at that platform and no one else, and the activity &#x60;\&quot;BOARD\&quot;&#x60; represents customers boarding at the informed entity, then the entity includes &#x60;activities&#x60; &#x60;[\&quot;BOARD\&quot;]&#x60;. If the alert affected customers exiting at the platform too, then &#x60;activities&#x60; is &#x60;[\&quot;BOARD\&quot;, \&quot;EXIT\&quot;]&#x60;.  It should be noted that the &#x60;activities&#x60; array includes activities that are specifically affected. Thus if there were activities &#x60;\&quot;BOARD\&quot;&#x60;, &#x60;\&quot;EXIT\&quot;&#x60;, and &#x60;\&quot;USING_WHEELCHAIR\&quot;&#x60; [to board or exit], and a station were closed, then the &#x60;activities&#x60; array would include &#x60;\&quot;BOARD\&quot;&#x60; and &#x60;\&quot;EXIT\&quot;&#x60; but it would not be necessary to include the activity &#x60;\&quot;USING_WHEELCHAIR\&quot;&#x60;. Any rider entering the station who is &#x60;\&quot;USING_WHEELCHAIR\&quot;&#x60; is also a rider who &#x60;\&quot;BOARD\&quot;&#x60;s. Using a wheelchair to board is not specifically affected.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


