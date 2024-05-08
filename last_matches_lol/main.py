def get_last_matches_ids(count):
    url = f"https://{region}.api.riotgames.com/lol/match/v5/matches/by-puuid/{PUUID}/ids?start=0&count={count}&api_key={API_KEY}"
    response = requests.get(url)

    with open(f"last_{count}_matches_ids.txt", "w") as file:
        json.dump(response.json(), file, indent=4)
        data = json.loads(response.text)
        last_matches_ids = pd.Series(data)
        file.close()

    return last_matches_ids


def get_last_matches(count):
    ids = get_last_matches_ids(count)

    for matchId in ids:
        url = f"https://{region}.api.riotgames.com/lol/match/v5/matches/{matchId}?api_key={API_KEY}"
        response = requests.get(url)

        newpath = f"last_{count}_matches"
        if not os.path.exists(newpath):
            os.makedirs(newpath)

        with open(f"last_{count}_matches/{matchId}.txt", "w") as file:
            json.dump(response.json(), file, indent=4)
            file.close()


if __name__ == '__main__':
    import requests
    import json
    import os
    import pandas as pd
    import numpy as np
    import matplotlib as plt

    API_KEY = "RGAPI-0b03c196-d121-4aaf-bc55-783c3a646d5a"

    region = "europe"
    subregion = "eun1"
    name = "6933369"
    tag = "putin"
    PUUID = "IpIff2Vl7VVyafVFQN-HizjiCC_sL7lqJP1jSASAujENb9Rx5k1KghVAZxtQZ8cLaHMsJ2K3eiDSnQ"

    get_last_matches(5)





