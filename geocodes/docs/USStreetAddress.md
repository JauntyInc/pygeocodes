# USStreetAddress


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**formatted** | **str** | The formatted version of the street address. | 
**street_name** | **str** | The street name of the address. This omits the road type. So the address &#39;101 Main Street&#39; would have &#39;Main&#39; in the StreetName field. | 
**number** | **str** | The number of the street address. It is important that this is stored in a string. Many valid house numbers cannot be represented by just a number, in which case the alphanumeric_number field will be populated: Some fake examples include &#39;1/2 Smith Street&#39;, &#39;41-13 39th Place&#39;, &#39;E400N200 Pike Street&#39;. Note that the alpha version of the API only includes numeric addresses, but our stable release will handle this\&quot; | [optional] 
**postdirectional** | **str** | A directional (N, E, S, W, etc) that appears after the street name. For example, &#39;W&#39; is the postdirectional in &#39;1 Main Street W&#39;. | [optional] 
**predirectional** | **str** | A directional (N, E, S, W, etc) that appears before the street name. For example, &#39;E&#39; is the predirectional in &#39;1 E Main Street&#39;. | [optional] 
**type** | **str** | The type of the street: Rd, St, Ave, etc. So the address &#39;101 Main Street&#39; would be &#39;St&#39;. May be omitted for some roads. For example, &#39;Broadway&#39; and &#39;The Embarcadero&#39; are valid road names that do not have road types. | [optional] 
**unit_designator** | **str** | A unit designator in an address, if one is present. For example, &#39;Apt 3&#39; is the unit designator in &#39;1 Main Street Apt 3&#39;. This may combine more than one designator into the same field: &#39;Building 2 Floor 1&#39;. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


