# database-prep/requests/latest_data.py

import requests
from dotenv import load_dotenv
import os
import json
import time
from token_module import access_token

load_dotenv()
api_key = os.getenv('API_KEY')

dams = [
    {"dam_name": "Toonumbar Dam", "dam_id": "203042"},
    {"dam_name": "Glenbawn Dam", "dam_id": "210097"},
    {"dam_name": "Lostock Dam", "dam_id": "210102"},
    {"dam_name": "Glennies Creek Dam", "dam_id": "210117"},
    {"dam_name": "Nepean Dam", "dam_id": "212205"},
    {"dam_name": "Avon Dam", "dam_id": "212211"},
    {"dam_name": "Wingecarribee Reservoir", "dam_id": "212212"},
    {"dam_name": "Cordeaux Dam", "dam_id": "212220"},
    {"dam_name": "Cataract Dam", "dam_id": "212232"},
    {"dam_name": "Warragamba Dam", "dam_id": "212243"},
    {"dam_name": "Woronora Dam", "dam_id": "213210"},
    {"dam_name": "Prospect Reservoir", "dam_id": "213240"},
    {"dam_name": "Tallowa Dam", "dam_id": "215212"},
    {"dam_name": "Fitzroy Falls Reservoir", "dam_id": "215235"},
    {"dam_name": "Brogo Dam", "dam_id": "219027"},
    {"dam_name": "Cochrane Dam", "dam_id": "219033"},
    {"dam_name": "Hume Dam", "dam_id": "401027"},
    {"dam_name": "Blowering Dam", "dam_id": "410102"},
    {"dam_name": "Burrinjuck Dam", "dam_id": "410131"},
    {"dam_name": "Lake Wyangala", "dam_id": "412010"},
    {"dam_name": "Carcoar Dam", "dam_id": "412106"},
    {"dam_name": "Lake Cargelligo", "dam_id": "412107"},
    {"dam_name": "Lake Brewster", "dam_id": "412108"},
    {"dam_name": "Pindari Dam", "dam_id": "416030"},
    {"dam_name": "Copeton Dam", "dam_id": "418035"},
    {"dam_name": "Keepit Dam", "dam_id": "419041"},
    {"dam_name": "Chaffey Dam", "dam_id": "419069"},
    {"dam_name": "Split Rock Dam", "dam_id": "419080"},
    {"dam_name": "Burrendong Dam", "dam_id": "421078"},
    {"dam_name": "Windamere Dam", "dam_id": "421148"},
    {"dam_name": "Oberon Dam", "dam_id": "421189"},
    {"dam_name": "Lake Menindee", "dam_id": "425022"},
    {"dam_name": "Lake Cawndilla", "dam_id": "425023"},
    {"dam_name": "Lake Wetherell", "dam_id": "425046"},
    {"dam_name": "Lake Tandure", "dam_id": "425047"},
    {"dam_name": "Lake Pamamaroo", "dam_id": "42510036"},
    {"dam_name": "Lake Copi Hollow", "dam_id": "42510037"},
]

url_template = "https://api.onegov.nsw.gov.au/waternsw-waterinsights/v1/dams/{}/resources/latest"

headers = {
    'Authorization': f'Bearer {access_token}',
    'apikey': api_key
}

all_data = []

def fetch_data(dam_name, dam_id, retries=3, timeout=10):
    url = url_template.format(dam_id)
    for attempt in range(retries):
        try:
            response = requests.get(url, headers=headers, timeout=timeout)
            if response.status_code == 200:
                return response.json()
            elif response.status_code == 204:
                print(f"No content available for {dam_name} (ID: {dam_id}).")
                return None
            else:
                print(f"Failed to retrieve data for {dam_name} (ID: {dam_id}): {response.status_code}")
        except requests.exceptions.Timeout:
            print(f"Request timeout for {dam_name} (ID: {dam_id}). Attempt {attempt + 1} of {retries}. Retrying...")
        time.sleep(2)
    return None

for dam in dams:
    data = fetch_data(dam['dam_name'], dam['dam_id'])
    if data:
        all_data.append({dam['dam_name']: data})

with open('./latest_dam_data.json', 'w') as json_file:
    json.dump(all_data, json_file, indent=4)

print("Data successfully written to latest_dam_data.json")
