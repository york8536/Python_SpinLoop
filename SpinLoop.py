import requests
import asyncio
import websockets
import json
import time
import SpinLoop_Config

# --------------------------------------------------------------------------------- api參數設定
req_login = { 
        "SiteID": SpinLoop_Config.siteID, 
        "DeviceID": SpinLoop_Config.deviceID, # ID:6666758868 WS也要改DeviceID
        "TPType": 1,
        "PlatID": 2, # PlatID   1:android   2:ios   3:web
        "Screen": "QATest"
    }

# --------------------------------------------------------------------------------- api
r = requests.post(SpinLoop_Config.siteURL, json = req_login) # 記得改環境
# r = requests.post('https://10.70.78.71/api/v1/login', json = req_login)
print(r)
print(r.content)
print('done')
FrontAPI_Login_Token=(r.json()["Result"]["Token"])

# -----------------------------------------------------------------------------ws參數設定
req_10000 = {
    "OP": 10000,
    "Token": FrontAPI_Login_Token,
    "DeviceID": SpinLoop_Config.deviceID,
    "Lang": "zh-tw",
    "CloseRSA": True
}

req_20010 = {
    "OP":20010,
    "GameCode":SpinLoop_Config.gameCode
}

req_20230 = {
    "OP": 20030,
    "Script": "script-QATest.json"
}

req_20020 = {
  "OP":20020,
  "PerPage": 1,
  "Multiplier": SpinLoop_Config.multiplier
}

req_20040 = {
    "OP": 20040
}
# -----------------------------------------------------------------------------websocket

# WebSocket服务器的地址
url = "ws://qphoenix.1161023.lol/ws/game" # 記得改環境

async def connect_ws():
    start_time = time.time()  # 開始記錄時間
    async with websockets.connect(url) as websocket:
        print("WebSocket 连接已建立")
        
        # 初始化
        req_10000_json = json.dumps(req_10000)
        await websocket.send(req_10000_json)
        print("Request sent (OP: 10000):", req_10000)
        
        # 接收服務的響應並印出
        response_10000 = await websocket.recv()
        print("Response (OP: 10000):", response_10000)

        
        # 進入遊戲
        req_20010_json = json.dumps(req_20010)
        await websocket.send(req_20010_json)
        print("Request sent (OP: 20010):", req_20010)
        
        # 接收服務的響應並印出
        response_20010 = await websocket.recv()
        print("Response (OP: 20010):", response_20010)

        for x in range(SpinLoop_Config.spinTimes):
            if SpinLoop_Config.script == True:
                # 使用數值腳本
                req_20230_json = json.dumps(req_20230)
                await websocket.send(req_20230_json)
                # print("Request sent (OP: 20230):", req_20230)
                # 接收服務的響應
                while True:
                    response_20230 = await websocket.recv() 
                    response_20230 = json.loads(response_20230)
                    if response_20230['Code'] == 200:
                        break

            # spin
            req_20020_json = json.dumps(req_20020)
            await websocket.send(req_20020_json)
            # print("Request sent (OP: 20020):", req_20020)
            
            while True:
            # 接收服務的響應並印出
                response_20020 = await websocket.recv()
                response_20020 = json.loads(response_20020)
                if response_20020['OP'] == 20021:
                    # print("Response (OP: 20020):", response_20020)
                    # print("Response (OP: 20020):", x+1)
                    break
                
            # settle
            req_20040_json = json.dumps(req_20040)
            await websocket.send(req_20040_json)
            # print("Request sent (OP: 20040):", req_20040)
            
            while True:
                # 接收服務的響應並印出
                response_20040 = await websocket.recv()
                response_20040 = json.loads(response_20040)
                if response_20040['OP'] == 20041:
                    # print("Response (OP: 20040):", response_20040)
                    # print("Response (OP: 20040):", x+1)
                    break
            print('spin次數',x+1)

        try:
            # 關閉 WebSocket 連線
            await websocket.close()
            print("WebSocket 連線已關閉")
        except websockets.exceptions.ConnectionClosed:
            print("WebSocket 連線關閉時發生錯誤")

        end_time = time.time()  # 結束記錄時間
        execution_time = end_time - start_time  # 計算執行時間
        print("函式執行時間:", execution_time, "秒")

# # 运行 WebSocket 客户端

asyncio.run(connect_ws())
