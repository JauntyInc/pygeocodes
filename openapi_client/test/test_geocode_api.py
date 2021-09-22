"""
    geo.codes

    The alpha version of the [https://geo.codes](https://geo.codes) API service. See API documentation [here](https://geo.codes/docs/api). 10,000 free queries per month.  # noqa: E501

    The version of the OpenAPI document: 1.0.0-alpha
    Contact: help@geo.codes
    Generated by: https://openapi-generator.tech
"""


import unittest

import openapi_client
from openapi_client.api.geocode_api import GeocodeApi  # noqa: E501


class TestGeocodeApi(unittest.TestCase):
    """GeocodeApi unit test stubs"""

    def setUp(self):
        self.api = GeocodeApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_v1_address_geocode(self):
        """Test case for v1_address_geocode

        Geocode an unstructured address string  # noqa: E501
        """
        pass

    def test_v1_address_reverse_zip_code(self):
        """Test case for v1_address_reverse_zip_code

        Convert a coordinate to a ZIP Code  # noqa: E501
        """
        pass

    def test_v1_address_structured_geocode(self):
        """Test case for v1_address_structured_geocode

        Geocode structured addresses  # noqa: E501
        """
        pass

    def test_v1_address_zip_code(self):
        """Test case for v1_address_zip_code

        Convert a ZIP Code to a coordinate  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()