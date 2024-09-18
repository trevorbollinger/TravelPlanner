import requests
import os
from django.shortcuts import render
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def api_demo(request):
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
    
    if not access_token:
        return render(request, 'error.html', {'message': 'Failed to get access token'})

    # Get nearby hotels using geocode
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

    print(api_data)
    
    if api_response.status_code == 200:
        return render(request, 'api_demo.html', {'data': api_data})
    else:
        return render(request, 'error.html', {'message': 'Failed to retrieve data'})