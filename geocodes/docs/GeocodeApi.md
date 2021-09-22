# geocodes.GeocodeApi

All URIs are relative to *https://api.geo.codes*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_address_geocode**](GeocodeApi.md#v1_address_geocode) | **GET** /v1/address/geocode | Geocode an unstructured address string
[**v1_address_reverse_zip_code**](GeocodeApi.md#v1_address_reverse_zip_code) | **GET** /v1/address/reverse_zip_code | Convert a coordinate to a ZIP Code
[**v1_address_structured_geocode**](GeocodeApi.md#v1_address_structured_geocode) | **GET** /v1/address/structured_geocode | Geocode structured addresses
[**v1_address_zip_code**](GeocodeApi.md#v1_address_zip_code) | **GET** /v1/address/zip_code | Convert a ZIP Code to a coordinate


# **v1_address_geocode**
> Geocoding v1_address_geocode(q)

Geocode an unstructured address string

**Description**<br><br>  Geocode a single address. This parses the input address and matches it against our records to produce the geocoded result.  This does a best-attempt to geocode the given address in the face of human errors in the input data. This can be the wrong city (\"New York City\" instead of \"New York\") a missing postal code, a misspelled street name, house numbers that don't exist, etc.  As more corrections are needed, the certainty in the result drops. This can be tuned with a minimum certainty parameter. If our confidence in the result is less than the minimum certainty, it will not be returned. The default is 30. 30 was chosen to be robust against unclean data without returning results that are unlikely to be true. We don't recommend setting this parameter above 90 because exact matching is too restrictive for the mistakes that people typically make when writing addresses -- even people writing their own addresses will make mistakes that are never corrected.  **Lookup cost**  This query requires an account. Please sign up at https://geo.codes/signup and get your API key at https://geo.codes/account/api  One query counts as one lookup. It only costs a query if it returns data. If you have exceeded your account quota, the request will not succeed.

### Example

* Api Key Authentication (ApiKeyHeaderAuth):
* Api Key Authentication (ApiKeyURLAuth):
```python
import time
import geocodes
from geocodes.api import geocode_api
from geocodes.model.geocoding import Geocoding
from pprint import pprint
# Defining the host is optional and defaults to https://api.geo.codes
# See configuration.py for a list of all supported configuration parameters.
configuration = geocodes.Configuration(
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
with geocodes.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = geocode_api.GeocodeApi(api_client)
    q = "q_example" # str | The unstructured address to geocode. Expected to be roughly the format that is used by the USPS to deliver mail.
    min_confidence = 1 # int | The minimum confidence in the results required to return an address, as a percentage between 0 and 100. Default: 30. To accept only exact data matches, choose 100. To be as permissive as possible, set it to 0. We don't recommend setting this higher than 90. It is very common for people to write their own addresses in ways that deviate from the exact match. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Geocode an unstructured address string
        api_response = api_instance.v1_address_geocode(q)
        pprint(api_response)
    except geocodes.ApiException as e:
        print("Exception when calling GeocodeApi->v1_address_geocode: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Geocode an unstructured address string
        api_response = api_instance.v1_address_geocode(q, min_confidence=min_confidence)
        pprint(api_response)
    except geocodes.ApiException as e:
        print("Exception when calling GeocodeApi->v1_address_geocode: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**| The unstructured address to geocode. Expected to be roughly the format that is used by the USPS to deliver mail. |
 **min_confidence** | **int**| The minimum confidence in the results required to return an address, as a percentage between 0 and 100. Default: 30. To accept only exact data matches, choose 100. To be as permissive as possible, set it to 0. We don&#39;t recommend setting this higher than 90. It is very common for people to write their own addresses in ways that deviate from the exact match. | [optional]

### Return type

[**Geocoding**](Geocoding.md)

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

# **v1_address_reverse_zip_code**
> ReverseZIPCode v1_address_reverse_zip_code(latitude, longitude)

Convert a coordinate to a ZIP Code

**Description**<br>  Look up a single ZIP Code from the given latitude and longitude.  This performs a lookup based on US Census \"ZIP Code Tabulation Areas.\" These areas are calculated by the US Census based on the most common ZIP Codes within different US Census blocks. This is necessary because in practice, ZIP Codes are not defined by areas but are defined as collections of addresses. They correspond loosely to areas, but not exactly. To get an accurate ZIP Code for an address, see the geocoding endpoints.  For more information on ZIP Code tabulation areas and why ZIP Codes cannot be accurately represented by areas, [click here](https://geo.codes/resources/articles/complete-guide-to-zip-codes#what-are-zip-code-tabulation-areas).  They have the following limitations: - ZIP Code Tabulation Areas do not have full coverage of the land mass of the United States. This only matters in remote areas without deliverable addresses; in practice this is fine. In these cases, the API will return the closest tabulation area unless the ` + \"`strict`\" + ` parameter is provided. - Addresses within a ZIP Code Tabulation Area might have different ZIP Codes. Geocoding an address is the only way to get a perfect ZIP Code. - The PlusFour field on the return value will always be empty.  **Lookup cost**<br>  This query requires an account. Please sign up at https://geo.codes/signup and get your API key at https://geo.codes/account/api  One query counts as one lookup. It only costs a query if it returns data. If you have exceeded your account quota, the request will not succeed.

### Example

* Api Key Authentication (ApiKeyHeaderAuth):
* Api Key Authentication (ApiKeyURLAuth):
```python
import time
import geocodes
from geocodes.api import geocode_api
from geocodes.model.reverse_zip_code import ReverseZIPCode
from pprint import pprint
# Defining the host is optional and defaults to https://api.geo.codes
# See configuration.py for a list of all supported configuration parameters.
configuration = geocodes.Configuration(
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
with geocodes.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = geocode_api.GeocodeApi(api_client)
    latitude = 3.14 # float | The latitude of the query
    longitude = 3.14 # float | The longitude of the query
    strict = True # bool | If true, will only return a result if the given point is within a zip code tabulation area, and will not return the closest one. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Convert a coordinate to a ZIP Code
        api_response = api_instance.v1_address_reverse_zip_code(latitude, longitude)
        pprint(api_response)
    except geocodes.ApiException as e:
        print("Exception when calling GeocodeApi->v1_address_reverse_zip_code: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Convert a coordinate to a ZIP Code
        api_response = api_instance.v1_address_reverse_zip_code(latitude, longitude, strict=strict)
        pprint(api_response)
    except geocodes.ApiException as e:
        print("Exception when calling GeocodeApi->v1_address_reverse_zip_code: %s\n" % e)
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

# **v1_address_structured_geocode**
> Geocoding v1_address_structured_geocode(street_address)

Geocode structured addresses

**Description**<br>  Geocode a single structured address. This takes address components (street, city, state, etc) and matches it against our records to produce the geocoded result.  This does a best-attempt to geocode the given address in the face of human errors in the input data. This can be the wrong city (\"New York City\" instead of \"New York\") a missing postal code, a misspelled street name, house numbers that don't exist, etc.  As more corrections are needed, the certainty in the result drops. This can be tuned with a minimum certainty parameter. If our confidence in the result is less than the minimum certainty, it will not be returned. The default is 30%. 30% was chosen to be robust against unclean data without returning results that are unlikely to be true. We don't recommend setting this parameter above 90% because exact matching is too restrictive for the mistakes that people typically make when writing addresses -- even people writing their own addresses will make mistakes that are never corrected because they Just Work.  **Lookup cost**<br>  This query requires an account. Please sign up at https://geo.codes/signup and get your API key at https://geo.codes/account/api  One query counts as one lookup. It only costs a query if it returns data. If you have exceeded your account quota, the request will not succeed.

### Example

* Api Key Authentication (ApiKeyHeaderAuth):
* Api Key Authentication (ApiKeyURLAuth):
```python
import time
import geocodes
from geocodes.api import geocode_api
from geocodes.model.geocoding import Geocoding
from pprint import pprint
# Defining the host is optional and defaults to https://api.geo.codes
# See configuration.py for a list of all supported configuration parameters.
configuration = geocodes.Configuration(
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
with geocodes.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = geocode_api.GeocodeApi(api_client)
    street_address = "street_address_example" # str | The street address line, including the number and street type.
    city = "city_example" # str | The city. Not required, but it's highly recommended that you add either the city or postal_code fields. (optional)
    state = "state_example" # str | The state with the address. Not required, but it's highly recommended that you add the postal_code if the state is not present. (optional)
    postal_code = "postal_code_example" # str | The postal code, for example, a ZIP code. Not required, but if this is not present, we recommend adding the city and the state for best results. (optional)
    min_confidence = 1 # int | The minimum confidence in the results required to return an address, as a percentage between 0 and 100. Default: 30. To accept only exact data matches, choose 100. To be as permissive as possible, set it to 0. We don't recommend setting this higher than 90. It is very common for people to write their own addresses in ways that deviate from the exact match. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Geocode structured addresses
        api_response = api_instance.v1_address_structured_geocode(street_address)
        pprint(api_response)
    except geocodes.ApiException as e:
        print("Exception when calling GeocodeApi->v1_address_structured_geocode: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Geocode structured addresses
        api_response = api_instance.v1_address_structured_geocode(street_address, city=city, state=state, postal_code=postal_code, min_confidence=min_confidence)
        pprint(api_response)
    except geocodes.ApiException as e:
        print("Exception when calling GeocodeApi->v1_address_structured_geocode: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **street_address** | **str**| The street address line, including the number and street type. |
 **city** | **str**| The city. Not required, but it&#39;s highly recommended that you add either the city or postal_code fields. | [optional]
 **state** | **str**| The state with the address. Not required, but it&#39;s highly recommended that you add the postal_code if the state is not present. | [optional]
 **postal_code** | **str**| The postal code, for example, a ZIP code. Not required, but if this is not present, we recommend adding the city and the state for best results. | [optional]
 **min_confidence** | **int**| The minimum confidence in the results required to return an address, as a percentage between 0 and 100. Default: 30. To accept only exact data matches, choose 100. To be as permissive as possible, set it to 0. We don&#39;t recommend setting this higher than 90. It is very common for people to write their own addresses in ways that deviate from the exact match. | [optional]

### Return type

[**Geocoding**](Geocoding.md)

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
import geocodes
from geocodes.api import geocode_api
from geocodes.model.zip_code import ZIPCode
from pprint import pprint
# Defining the host is optional and defaults to https://api.geo.codes
# See configuration.py for a list of all supported configuration parameters.
configuration = geocodes.Configuration(
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
with geocodes.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = geocode_api.GeocodeApi(api_client)
    zip_code = "zip_code_example" # str | The ZIP Code of the query. Can be a ZIP Code or a ZIP+4 Code. If a +4 extension is passed, it will be ignored.

    # example passing only required values which don't have defaults set
    try:
        # Convert a ZIP Code to a coordinate
        api_response = api_instance.v1_address_zip_code(zip_code)
        pprint(api_response)
    except geocodes.ApiException as e:
        print("Exception when calling GeocodeApi->v1_address_zip_code: %s\n" % e)
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

