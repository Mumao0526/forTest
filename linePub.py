import requests

url = "https://notify-api.line.me/api/notify"   # Line Notify服務
token = "HMEwxOLttiRbMvCiUvXcc0qIP3ly4YqynOcekhrK3gC"

headers = {"Authorization": "Bearer " + token}  # 設定token
data = {"message": "\n測試一下！"}  # 設定要發送的訊息
try:
    data = requests.post(url, headers=headers, data=data)  # 使用 POST 方法
    print("Line 通知推送成功")
except Exception as e:
    print(e.__traceback__)
