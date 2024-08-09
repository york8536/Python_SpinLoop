import requests
import json



# r = requests.post('https://sphoenix.089453.fun/api/v1/login', json = data_login)
# print(r.status_code)
# print(r.content)
for id in range(20):
    data_login = { # 參數設定
        "SiteID": "qat", # 記得改環境
        "DeviceID": f"qatest_20240726_{id}",
        "TPType": 1,
        "PlatID": 2, # PlatID   1:android   2:ios   3:web
        "Screen": "QATest"
    }
    r = requests.post('https://qphoenix.1161023.lol/api/v1/login', json = data_login) # 記得改環境
    print(r)
    print(r.content)    
print('done')
