import json
import os

def read_json_file(file_path):
    with open(file_path, 'r') as json_file:
        data = json.load(json_file)
    return data

# Usage
data = read_json_file('./data.json')

for item in data['data']:
    print(item)
    # def fileExists = fileExists "${env.WORKSPACE}/../${item}/microservices/webbff/test/e2e/goReportJSONFile/getProduct_output.json"
    file_path = f"../{item}/microservices/webbff/test/e2e/goReportJSONFile/getProduct_output.json"
    if os.path.exists(file_path):
        print(f"File '{file_path}' exists.")
    else:
        print(f"File '{file_path}' does not exist.")