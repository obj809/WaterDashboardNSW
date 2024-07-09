# database-prep/requests/collect_all_data.py

import requests
from dotenv import load_dotenv
import os
import json
from token_module import access_token

load_dotenv()
authorization_header = os.getenv('AUTHORIZATION_HEADER')
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
    {"dam_name": "Toonumbar Dam", "dam_id": "203042"},
    {"dam_name": "Glenbawn Dam", "dam_id": "210097"},
    {"dam_name": "Lostock Dam", "dam_id": "210102"},
    {"dam_name": "Glennies Creek Dam", "dam_id": "210117"},
    {"dam_name": "Nepean Dam", "dam_id": "212205"},
    {"dam_name": "Avon Dam", "dam_id": "212211"}
]

from_date = '1950-01-01'
to_date = '2024-06-30'

url_template = "https://api.onegov.nsw.gov.au/waternsw-waterinsights/v1/dams/{}/resources"
querystring = {"from": from_date, "to": to_date}
headers = {
    'authorization': f'Bearer {access_token}',
    'apikey': api_key
}

all_data = []

for dam in dams:
    dam_id = dam['dam_id']
    url = url_template.format(dam_id)
    response = requests.request("GET", url, headers=headers, params=querystring)
    
    if response.status_code == 200:
        data = response.json()
        all_data.append({dam['dam_name']: data})
    else:
        print(f"Failed to retrieve data for {dam['dam_name']}: {response.status_code}")

with open('./all_dam_data.json', 'w') as json_file:
    json.dump(all_data, json_file, indent=4)

print("Data successfully written to all_dam_data.json")
