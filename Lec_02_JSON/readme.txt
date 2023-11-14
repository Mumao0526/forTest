目標：
    在"doit_5_2.json"中，撈出特定Barcode的所有時間戳記

By JAVA (ja_copy.java)
    . use jsonFileToString() get JSON file and transfer to String type
    . Take this String to be a JSONArray type by JSONArray which in third-party library named java-json.jar
    . Get JSONObject in JSONArray, and get the value by the key

By PYTHON (jsonprocesse.py)
    . Open doit_5_2.json file
    . Use json.load() to get data by json format