# openapi_client.ZipCodeApi

All URIs are relative to *https://api.geo.codes*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_address_reverse_zip_code**](ZipCodeApi.md#v1_address_reverse_zip_code) | **GET** /v1/address/reverse_zip_code | Convert a coordinate to a ZIP Code
[**v1_address_zip_code**](ZipCodeApi.md#v1_address_zip_code) | **GET** /v1/address/zip_code | Convert a ZIP Code to a coordinate


# **v1_address_reverse_zip_code**
> ReverseZIPCode v1_address_reverse_zip_code(latitude, longitude)

Convert a coordinate to a ZIP Code

**Description**<br>  Look up a single ZIP Code from the given latitude and longitude.  This performs a lookup based on US Census \"ZIP Code Tabulation Areas.\" These areas are calculated by the US Census based on the most common ZIP Codes within different US Census blocks. This is necessary because in practice, ZIP Codes are not defined by areas but are defined as collections of addresses. They correspond loosely to areas, but not exactly. To get an accurate ZIP Code for an address, see the geocoding endpoints.  For more information on ZIP Code tabulation areas and why ZIP Codes cannot be accurately represented by areas, [click here](https://geo.codes/resources/articles/complete-guide-to-zip-codes#what-are-zip-code-tabulation-areas).  They have the following limitations: - ZIP Code Tabulation Areas do not have full coverage of the land mass of the United States. This only matters in remote areas without deliverable addresses; in practice this is fine. In these cases, the API will return the closest tabulation area unless the ` + \"`strict`\" + ` parameter is provided. - Addresses within a ZIP Code Tabulation Area might have different ZIP Codes. Geocoding an address is the only way to get a perfect ZIP Code. - The PlusFour field on the return value will always be empty.  **Lookup cost**<br>  This query requires an account. Please sign up at https://geo.codes/signup and get your API key at https://geo.codes/account/api  One query counts as one lookup. It only costs a query if it returns data. If you have exceeded your account quota, the request will not succeed.

### Example

* Api Key Authentication (ApiKeyHeaderAuth):
* Api Key Authentication (ApiKeyURLAuth):
```python
import time
import openapi_client
from openapi_client.api import zip_code_api
from openapi_client.model.reverse_zip_code import ReverseZIPCode
from pprint import pprint
# Defining the host is optional and defaults to https://api.geo.codes
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.geo.codes"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyHeaderAuth
configuration.api_key['ApiKeyHeaderAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyHeaderAuth'] = 'Bearer'

# Configure API key authorization: ApiKeyURLAuth
configuration.api_key['ApiKeyURLAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyURLAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = zip_code_api.ZipCodeApi(api_client)
    latitude = 3.14 # float | The latitude of the query
    longitude = 3.14 # float | The longitude of the query
    strict = True # bool | If true, will only return a result if the given point is within a zip code tabulation area, and will not return the closest one. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Convert a coordinate to a ZIP Code
        api_response = api_instance.v1_address_reverse_zip_code(latitude, longitude)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ZipCodeApi->v1_address_reverse_zip_code: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Convert a coordinate to a ZIP Code
        api_response = api_instance.v1_address_reverse_zip_code(latitude, longitude, strict=strict)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ZipCodeApi->v1_address_reverse_zip_code: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **latitude** | **float**| The latitude of the query |
 **longitude** | **float**| The longitude of the query |
 **strict** | **bool**| If true, will only return a result if the given point is within a zip code tabulation area, and will not return the closest one. | [optional]

### Return type

[**ReverseZIPCode**](ReverseZIPCode.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth), [ApiKeyURLAuth](../README.md#ApiKeyURLAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_address_zip_code**
> ZIPCode v1_address_zip_code(zip_code)

Convert a ZIP Code to a coordinate

**Description**<br>  Convert a single ZIP Code into a latitude and longitude.  By default, this returns a point that is guaranteed to be interior to the given ZIP Code. It may not necessarily be the centroid, because the centroid of some ZIP Codes do not fall within their borders (imagine a ZIP Code that is shaped like a crescent).  If a Plus-4 ZIP code is passed, only the first 5 digits will be used (i.e. the +4 will be ignored).  This performs a lookup based on US Census \"ZIP Code Tabulation Areas.\" These areas are calculated by the US Census based on the most common ZIP Codes within different US Census blocks. This is necessary because in practice, ZIP Codes are not defined by areas but are defined as collections of addresses. They correspond loosely to areas, but not exactly. To get an accurate ZIP Code for an address, see the geocoding endpoints.  For more information on ZIP Code tabulation areas and why ZIP Codes cannot be accurately represented by areas, [click here](https://geo.codes/resources/articles/complete-guide-to-zip-codes#what-are-zip-code-tabulation-areas).

### Example

* Api Key Authentication (ApiKeyHeaderAuth):
* Api Key Authentication (ApiKeyURLAuth):
```python
import time
import openapi_client
from openapi_client.api import zip_code_api
from openapi_client.model.zip_code import ZIPCode
from pprint import pprint
# Defining the host is optional and defaults to https://api.geo.codes
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.geo.codes"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyHeaderAuth
configuration.api_key['ApiKeyHeaderAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyHeaderAuth'] = 'Bearer'

# Configure API key authorization: ApiKeyURLAuth
configuration.api_key['ApiKeyURLAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyURLAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = zip_code_api.ZipCodeApi(api_client)
    zip_code = "zip_code_example" # str | The ZIP Code of the query. Can be a ZIP Code or a ZIP+4 Code. If a +4 extension is passed, it will be ignored.

    # example passing only required values which don't have defaults set
    try:
        # Convert a ZIP Code to a coordinate
        api_response = api_instance.v1_address_zip_code(zip_code)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ZipCodeApi->v1_address_zip_code: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zip_code** | **str**| The ZIP Code of the query. Can be a ZIP Code or a ZIP+4 Code. If a +4 extension is passed, it will be ignored. |

### Return type

[**ZIPCode**](ZIPCode.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth), [ApiKeyURLAuth](../README.md#ApiKeyURLAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

