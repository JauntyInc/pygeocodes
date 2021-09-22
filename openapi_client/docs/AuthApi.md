# openapi_client.AuthApi

All URIs are relative to *https://api.geo.codes*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_test**](AuthApi.md#v1_test) | **GET** /v1/test | Ping function that tests the API Key


# **v1_test**
> str v1_test()

Ping function that tests the API Key

**Description**  An endpoint that always responds with the string `authorized!` when authentication works. This can be used as a check that the authentication on a request is valid.  Please include your key on the `Authorization` header or the query parameter `api_key`  **No account required**  This endpoint requires an account to be accessed, but does not count as a lookup. Requests may still be rejected due to rate limiting by any facet (account, IP, etc), in order to preserve the health of the service.

### Example

* Api Key Authentication (ApiKeyHeaderAuth):
* Api Key Authentication (ApiKeyURLAuth):
```python
import time
import openapi_client
from openapi_client.api import auth_api
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
    api_instance = auth_api.AuthApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Ping function that tests the API Key
        api_response = api_instance.v1_test()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AuthApi->v1_test: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**str**

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth), [ApiKeyURLAuth](../README.md#ApiKeyURLAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | authorized! |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

