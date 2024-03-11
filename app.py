import json

def read_json_file(file_path):
    with open(file_path, 'r') as json_file:
        data = json.load(json_file)
    return data

# Usage
data = read_json_file('./data.json')

for item in data['data']:
    print(item)
    