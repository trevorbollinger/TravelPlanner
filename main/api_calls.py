import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def get_token():
    client_id = os.getenv('AMADEUS_CLIENT_ID')
    client_secret = os.getenv('AMADEUS_CLIENT_SECRET')

    token_url = 'https://test.api.amadeus.com/v1/security/oauth2/token'
    token_data = {
        'grant_type': 'client_credentials',
        'client_id': client_id,
        'client_secret': client_secret
    }
    token_headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    response = requests.post(token_url, data=token_data, headers=token_headers)
    token_info = response.json()
    access_token = token_info.get('access_token')
    return access_token

access_token = get_token()

def get_hotels():
    api_url = 'https://test.api.amadeus.com/v1/reference-data/locations/hotels/by-geocode'
    api_params = {
        'latitude': '41.247219258801884',
        'longitude': '-96.01676854329351',
        'radius': '3',
        'radiusUnit': 'MILE',
        'hotelSource': 'ALL'
    }
    api_headers = {
        'Authorization': f'Bearer {access_token}'
    }

    api_response = requests.get(api_url, params=api_params, headers=api_headers)
    api_data = api_response.json()

    #print(api_data)
    return api_data

def get_attrs():
    api_url = 'https://test.api.amadeus.com/v1/shopping/activities'
    api_params = {
        'latitude': '41.247219258801884',
        'longitude': '-96.01676854329351',
        'radius': '3',
    }
    api_headers = {
        'Authorization': f'Bearer {access_token}'
    }

    api_response = requests.get(api_url, params=api_params, headers=api_headers)
    api_data = api_response.json()

    #print(api_data)
    return api_data
