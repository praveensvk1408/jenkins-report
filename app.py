import json
import os
from datetime import datetime

def read_json_file(file_path):
    with open(file_path, 'r') as json_file:
        data = json.load(json_file)
    return data

# Usage
data = read_json_file('./jobs.json')
passCount=0
failCount=0
totalCount=0
for item in data['data']:
    print(item)
    # def fileExists = fileExists "${env.WORKSPACE}/../${item}/microservices/webbff/test/e2e/goReportJSONFile/getProduct_output.json"
    file_path = f"../{item}/microservices/webbff/test/e2e/goReportJSONFile/getProduct_output.json"
    if os.path.exists(file_path):
        print(f"File '{file_path}' exists.")
        filedata = read_json_file(file_path)
        passCount+=filedata['successNum']
        failCount+=filedata['failNum']
        totalCount+=filedata['totalNum']
    else:
        print(f"File '{file_path}' does not exist.")

print(f"Total Pass: {passCount}")
print(f"Total Fail: {failCount}")
print(f"Total Count: {totalCount}")

current_date = datetime.now().strftime("%d-%m-%Y")
print(f"Current Date: {current_date}")

if os.path.exists("data.json"):
    jsondata = read_json_file("data.json")
    dataobj = {
        "pass" : passCount,
        "fail" : failCount,
        "total" : totalCount
    }
    # if current_date in jsondata:
    #     print("Key exists in jsondata.")
    jsondata[current_date] = dataobj
    # else:
        # print("Key does not exist in jsondata.")
        # jsondata[current_date] = dataobj
    # overwite the json file with the updated data
    with open("data.json", 'w') as json_file:
        json.dump(jsondata, json_file) 
else:
    print("File 'data.json' does not exist.")
    dataobj = {
        "pass" : passCount,
        "fail" : failCount,
        "total" : totalCount
    }
    jsondata = {}
    jsondata[current_date] = dataobj
    with open("data.json", 'w') as json_file:
        json.dump(jsondata, json_file)