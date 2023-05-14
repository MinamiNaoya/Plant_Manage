import requests


# 020000が青森のエリアコード
url = "https://www.jma.go.jp/bosai/forecast/data/forecast/020000.json"



header= {"content-type": "application/json"}
r = requests.get(url, headers=header)

data = r.json()

WETHER_CODE = {"200": "曇りところにより雨", "202": "曇り 昼過ぎ 一時 雨", "200": "くもり"}
AREA_CODE = {"020030":"三八上北", "020010":"津軽", "020020":"下北"}

three_days = data[0]
seven_days = data[1]


today = three_days["timeSeries"][0]

tomorrow = three_days["timeSeries"][1]
day_after_tommorow = three_days["timeSeries"][2]

today_sanpaticamikita = today["areas"][2]
today_simokita = today["areas"][1]
today_tsugaru = today["areas"][0]


today_sanpaticamikita_weathercode = today_sanpaticamikita["weatherCodes"][0]


