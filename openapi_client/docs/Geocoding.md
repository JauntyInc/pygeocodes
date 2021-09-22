# Geocoding


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**confidence** | **int** | The confidence that the address was correctly geocoded. Range 0-100. 100 was an exact record match, 0 is a wild guess. | 
**dataset_citation_required** | **bool** | Whether the original data source requires citation via their license terms. This is not used at the moment, but will be in the future. | 
**matched_address** | [**USAddress**](USAddress.md) |  | 
**result_dataset** | **str** | The dataset that the result was derived from. | 
**result_location** | **str** | The description of where the point is. At the moment, all of the points are offset from the road, but in the future this will additionally include rooftop and entrance locations. | 
**result_type** | **str** | Describes how the location was derived. All geocodings are interpolated at the moment, but in the future this will include direct lookups. | 
**coordinate** | [**GCSCoordinate**](GCSCoordinate.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


