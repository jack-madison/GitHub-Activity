import json

with open("2020-01-01-15.json") as jsonFile:
    jsonObject = json.load(jsonFile)
    jsonFile.close()