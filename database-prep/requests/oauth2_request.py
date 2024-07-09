# database-prep/requests/oauth2_request.py

import requests
from dotenv import load_dotenv
import os

load_dotenv()
authorization_header = os.getenv('AUTHORIZATION_HEADER')

url = "https://api.onegov.nsw.gov.au/oauth/client_credential/accesstoken"
querystring = {"grant_type":"client_credentials"}

headers = {'authorization': authorization_header}

response = requests.request("GET", url, headers=headers, params=querystring)
response_data = response.json()

access_token = response_data['access_token']

print(response_data)
print(access_token)

with open('./requests/token_module.py', 'w') as file:
    file.write(f"access_token = '{access_token}'\n")

print("Access token saved to module.")
