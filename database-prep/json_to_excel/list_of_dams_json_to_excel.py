# database-prep/json_to_excel/list_of_dams_json_to_excel.py

import json
import pandas as pd

def load_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

file_path = './database-prep/list_of_dams.json'
json_data = load_json(file_path)

data = []

for dam in json_data['dams']:
    data.append({
        'dam_id': dam['dam_id'],
        'dam_name': dam['dam_name'],
        'full_volume': dam['full_volume'],
        'lat': dam['lat'],
        'long': dam['long']
    })

df = pd.DataFrame(data)

output_file_path = './json_to_excel/data/list_of_dams.xlsx'
df.to_excel(output_file_path, index=False)

print(f"Data has been successfully converted to an Excel file: {output_file_path}")
