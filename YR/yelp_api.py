import argparse
import json
import pprint
import requests
import sys
import urllib

try:
    # For Python 3.0 and later
    from urllib.error import HTTPError
    from urllib.parse import quote
    from urllib.parse import urlencode
except ImportError:
    # Fall back to Python 2's urllib2 and urllib

    from urllib import quote
    from urllib import urlencode

API_KEY= "p5XJewjpIhpiwegBmHG-dETXNCdQst3XaDxu6iubyTvAWjYGrHoVLQxmcIVfTDRVwLkzujm1M8_8Dz2LhKh8etCa3HzwwAdm4zEFWDcDL-ebocrgJzLJZYWHxWu2XXYx"


categories="Food,Restaurants"

src_latitude=36.090671
src_longitude=-115.179614

dest_latitude=36.131742
dest_longitude=-115.180300

# API constants, you shouldn't have to change these.
API_HOST = 'https://api.yelp.com'
SEARCH_PATH = '/v3/businesses/search'
BUSINESS_PATH = '/v3/businesses/'  # Business ID will come after slash.

# Defaults for our simple example.
# DEFAULT_TERM = 'dinner'
# DEFAULT_LOCATION = 'San Francisco, CA'
SEARCH_LIMIT = 20

def request(host, path, api_key, url_params=None):
    """Given your API_KEY, send a GET request to the API.
    Args:
        host (str): The domain host of the API.
        path (str): The path of the API after the domain.
        API_KEY (str): Your API Key.
        url_params (dict): An optional set of query parameters in the request.
    Returns:
        dict: The JSON response from the request.
    Raises:
        HTTPError: An error occurs from the HTTP request.
    """
    url_params = url_params or {}
    url = '{0}{1}'.format(host, quote(path.encode('utf8')))
    headers = {
        'Authorization': 'Bearer %s' % api_key,
    }

    print(u'Querying {0} ...'.format(url))

    response = requests.request('GET', url, headers=headers, params=url_params)

    return response.json()


def search_restaurants(src_latitude, src_longitude, dest_latitude, dest_longitude):
    url_params_src = {
        'latitude': src_latitude,
        'longitude': src_longitude,
        'limit': SEARCH_LIMIT,
        'categories': categories
    }
    url_params_dest = {
        'latitude': dest_latitude,
        'longitude': dest_longitude,
        'limit': SEARCH_LIMIT,
        'categories': categories
    }
    res_src = request(API_HOST, SEARCH_PATH, API_KEY, url_params=url_params_src)
    res_dest = request(API_HOST, SEARCH_PATH, API_KEY, url_params=url_params_dest)

    src_businesses = res_src['businesses']
    dest_businesses = res_dest['businesses']

    sids = []
    dids = []

    for sb in src_businesses:
        sids.append(sb['id'])

    for db in dest_businesses:
        dids.append(db['id'])


    print(sids)
    print(len(sids))
    print('$'*100)

    print(dids)
    print(len(dids))

    all_ids = sids + dids

    print(len(all_ids))

    return all_ids

def get_yelp_businesses():
    return search_restaurants(src_latitude, src_longitude, dest_latitude, dest_longitude)



