# geocodes.DefaultApi

All URIs are relative to *https://api.geo.codes*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ping**](DefaultApi.md#ping) | **GET** /ping | Ping the service without credentials


# **ping**
> str ping()

Ping the service without credentials

An endpoint that always responds with the string \"pong\". This can be used as a health check.<br><br>  This endpoint does not require an account to be accessed, and does not count as a lookup. Requests may still be rejected due to rate limiting to preserve the health of the service.  Alpha of Version 1 of the geo.codes API. Once V1 is stabilized, routes under `/v1` are guaranteed to follow semver-style backwards compatibility guarantees.

### Example

```python
import time
import geocodes
from geocodes.api import default_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.geo.codes
# See configuration.py for a list of all supported configuration parameters.
configuration = geocodes.Configuration(
    host = "https://api.geo.codes"
)


# Enter a context with an instance of the API client
with geocodes.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Ping the service without credentials
        api_response = api_instance.ping()
        pprint(api_response)
    except geocodes.ApiException as e:
        print("Exception when calling DefaultApi->ping: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The string &#39;pong&#39; |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

