import requests
import json
import pandas as pd
import numpy as np
import matplotlib as plt

API_KEY = "RGAPI-0b03c196-d121-4aaf-bc55-783c3a646d5a"

region = "europe"
subregion = "eun1"
name = "6933369"
tag = "putin"
PUUID = "IpIff2Vl7VVyafVFQN-HizjiCC_sL7lqJP1jSASAujENb9Rx5k1KghVAZxtQZ8cLaHMsJ2K3eiDSnQ"


url = f"https://{region}.api.riotgames.com/lol/match/v5/matches/by-puuid/{PUUID}/ids?start=0&count=1&api_key={API_KEY}"
response = requests.get(url)

with open(f"last_1_matches_ids.txt", "w") as file:
    json.dump(response.json(), file, indent=4)
    data_json = response.text
    data = json.loads(data_json)
    df = pd.Series(data)
    file.close()

print(df)