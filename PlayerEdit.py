import requests
import json


#-------------------------------------------------------------------------------------------登入後台取的token

Player_login = { # 參數設定
    "SiteID": "qat",
    "Account": "york0001",
    "Password": "1a5645e54d6aabed665494308a728014"
}
r_login = requests.post('https://qvirgo.1161023.lol/api/v1/login', json = Player_login) # 發出請求
# print(r_login.status_code)
token = r_login.json()["Result"]["APIToken"] # 撈出res中的 token

#-------------------------------------------------------------------------------------------叫出玩家列表
Player_list = { # 參數設定
    "Identity": [2], # 身份別 1: 正式 2: 測試
    "lastLoginTime": { 
        "StartTime": "2023-12-20T00:00:00+08:00",
        "EndTime": "2023-12-21T00:00:00+08:00"
    },
    "Page": 1,
    "Perpage": 10 # 資料筆數
}
headers = {
    'api-token' : token,
    'close-rsa': 'true'
}
Pids=[]

r_list = requests.post('https://qvirgo.1161023.lol/api/v1/player/list', json = Player_list,headers= headers) # 發出請求
# print(r_list.content)
playerList = r_list.json()["Result"]["PlayerList"]
for Playerid in playerList:
    Pids.append(Playerid["PlayerID"])
print(Pids) # 印出所有PlayerID

#-------------------------------------------------------------------------------------------更改玩家狀態
headers = {
    'api-token' : token,
    'close-rsa': 'true'
}

for Pid in Pids:
    Player_Edit = { # 參數設定
        "PlayerID": f"{Pid}",
        "Status": 1,
        "Identity": 1
    }
    r_edit = requests.post('https://qvirgo.1161023.lol/api/v1/player/edit', json = Player_Edit, headers= headers) # 發出請求
    print(r_edit.status_code)
    
print('done') # 執行完畢




