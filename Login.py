import requests
import json



# r = requests.post('https://sphoenix.089453.fun/api/v1/login', json = data_login)
# print(r.status_code)
# print(r.content)
for id in range(1):
    data_login = { # 參數設定
        "SiteID": "str",
        "DeviceID": f"qatest_01111_{id}",
        "TPType": 1,
        "PlatID": 2, # PlatID   1:android   2:ios   3:web
        "Screen": "QATest"
    }
    r = requests.post('https://sphoenix.089453.fun/api/v1/login', json = data_login)
    print(r)
    print(r.content)    
print('done')
