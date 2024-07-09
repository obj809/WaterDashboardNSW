# database-prep/requests/list_of_dams.py

import requests
from dotenv import load_dotenv
import os
import json
from token_module import access_token

load_dotenv()
api_key = os.getenv('API_KEY')

url = "https://api.onegov.nsw.gov.au/waternsw-waterinsights/v1/dams"

headers = {
    'authorization': f'Bearer {access_token}',
    'apikey': api_key
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    with open('./list_of_dams.json', 'w') as json_file:
        json.dump(data, json_file, indent=4)
    print("Response data successfully written to list_of_dams.json")
else:
    print(f"Failed to retrieve data: {response.status_code} - {response.text}")
