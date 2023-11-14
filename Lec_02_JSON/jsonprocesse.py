import json

with open("doit_5_2.json", "r", encoding="UTF-8") as f:
    jsonFile = json.load(f)
    requFile = []

    for item in jsonFile:
        if item["Barcode"] == "95M00031":
            requFile.append(item)

    if requFile:
        with open("output.json", "w", encoding="UTF-8") as f:
            json.dump(requFile, f)
