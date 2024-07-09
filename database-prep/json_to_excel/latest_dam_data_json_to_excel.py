# database-prep/json_to_excel/latest_dam_data_json_to_excel.py

import json
import pandas as pd

def load_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

file_path = './database-prep/latest_dam_data.json'
json_data = load_json(file_path)

data = []

for dam_info in json_data:
    for dam_name, dam_data in dam_info.items():
        dam_id = dam_data['dams'][0]['dam_id']
        dam_name = dam_data['dams'][0]['dam_name']
        resources = dam_data['dams'][0]['resources']
        
        for resource in resources:
            resource['dam_id'] = dam_id
            resource['dam_name'] = dam_name
            data.append(resource)

df = pd.DataFrame(data)

cols = ['dam_id', 'dam_name'] + [col for col in df if col not in ['dam_id', 'dam_name']]
df = df[cols]

output_file_path = './json_to_excel/data/latest_dam_data.xlsx'
df.to_excel(output_file_path, index=False)

print(f"Data has been successfully converted to an Excel file: {output_file_path}")
