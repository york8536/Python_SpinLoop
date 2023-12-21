import requests
import json



# r = requests.post('https://qphoenix.1161023.lol/api/v1/login', json = data_login)
# print(r.status_code)
# print(r.content)
for id in range(10):
    data_login = { # 參數設定
        "SiteID": "qat",
        "DeviceID": f"qatest_1219_{id}",
        "TPType": 1,
        "PlatID": 3, # PlatID   1:android   2:ios   3:web
        "Screen": "QATest"
    }
    r = requests.post('https://qphoenix.1161023.lol/api/v1/login', json = data_login)
    print(r)
    # print(r.content)    
print('done')
