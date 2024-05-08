""""

Check README.md


"""


def show_menu():
    print("Choose your region:")
    print("[1] Brazil")
    print("[2] Europe Nordic & East")
    print("[3] Europe West")
    print("[4] Latin America North")
    print("[5] Latin America South")
    print("[6] North America")
    choice = int(input("=> "))

    if choice == 1:
        return "americas", "br1"
    elif choice == 2:
        return "europe", "eun1"
    elif choice == 3:
        return "europe", "euw1"
    elif choice == 4:
        return "americas", "la1"
    elif choice == 5:
        return "americas", "la1"
    elif choice == 6:
        return "americas", "na1"
    else:
        # TODO: Make error
        return "unknown", "unknown"


def get_name_tag():
    name = input("Enter your in game username: ").strip()
    tag = input("Enter your name tag (without #): ").strip()

    return name, tag


def get_account_info():
    # Get the account info
    url = f"https://{region}.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{name}/{tag}?api_key={API_KEY}"
    response = requests.get(url)
    account_data = json.loads(response.text)

    # Save info to file
    with open(f"user_{name}_{tag}.json", "w") as f:
        json.dump(response.json(), f, indent=4)
        f.close()

    return account_data["puuid"]


def get_last_matches_ids():
    url = f"https://{region}.api.riotgames.com/lol/match/v5/matches/by-puuid/{PUUID}/ids?start=0&count={count}&api_key={API_KEY}"
    response = requests.get(url)

    with open(f"last_{count}_matches_ids.txt", "w") as file:
        json.dump(response.json(), file, indent=4)
        data = json.loads(response.text)
        last_matches_ids = pd.Series(data)
        file.close()

    return last_matches_ids


def get_last_matches():
    ids = get_last_matches_ids()

    for matchId in ids:
        url = f"https://{region}.api.riotgames.com/lol/match/v5/matches/{matchId}?type=ranked&api_key={API_KEY}"
        response = requests.get(url)

        newpath = f"last_{count}_matches"
        if not os.path.exists(newpath):
            os.makedirs(newpath)

        with open(f"last_{count}_matches/{matchId}.txt", "w") as file:
            json.dump(response.json(), file, indent=4)
            file.close()


def print_match_selector():
    mypath = f"last_{count}_matches"
    all_matches_ids = [f.rsplit(".", 1)[0].strip() for f in os.listdir(mypath) if os.path.isfile(os.path.join(mypath, f))]

    print("\n=== SELECT MATCH ===")
    num = 1
    for matchId in all_matches_ids:
        print(f"[{num}] {matchId}")
        num += 1
    print("--------------------")
    choice = int(input("=> "))

    return all_matches_ids[choice - 1]


def print_participants_stats():
    matchId = print_match_selector()
    match_path = f"last_5_matches/{matchId}.txt"

    df = pd.read_json(match_path)["info"]
    players_info = pd.json_normalize(df["participants"])[
        ["kills", "deaths", "assists", "riotIdGameName", "championName", "teamId", "firstBloodKill", "baronKills", "dragonKills", "goldEarned", "turretKills", "win", "totalDamageDealt", "totalDamageTaken", "totalMinionsKilled", "damageDealtToTurrets"]]

    players_info['kda'] = round((players_info["kills"] + players_info["assists"]) / players_info["deaths"], 2)

    my_player = players_info[players_info["riotIdGameName"] == name]

    print("\n==== Did you win? ====")
    if my_player[my_player["win"] == True].empty:
        print(f"- You didn't win the match")
    else:
        print(f"+ You won the match")

    team_1 = players_info[players_info["teamId"] == 100]
    team_2 = players_info[players_info["teamId"] == 200]


    print("\n==== TEAM 1 ====")
    print(f"Total barons: {team_1['baronKills'].sum()}")
    print(f"Total dragons: {team_1['dragonKills'].sum()}")
    print(f"Total gold earned: {team_1['goldEarned'].sum()}")
    print(f"Total turrets: {team_1['turretKills'].sum()}")
    print("-------------------------------------------------")
    for index, player in team_1.iterrows():
        print(
            f"{player['kills']}/{player['deaths']}/{player['assists']} ({player['kda']}) - {player['riotIdGameName']} ({player['championName']}) ")

    print("\n==== TEAM 2 ====")
    print(f"Total barons: {team_2['baronKills'].sum()}")
    print(f"Total dragons: {team_2['dragonKills'].sum()}")
    print(f"Total gold earned: {team_2['goldEarned'].sum()}")
    print(f"Total turrets: {team_2['turretKills'].sum()}")
    print("-------------------------------------------------")
    for index, player in team_2.iterrows():
        print(
            f"{player['kills']}/{player['deaths']}/{player['assists']} ({player['kda']}) - {player['riotIdGameName']} ({player['championName']}) ")

    first_blood = players_info[players_info["firstBloodKill"] == True]
    print("\n==== FIRST BLOOD ====")
    print(f"{first_blood['riotIdGameName'].iloc[0]} ({first_blood['championName'].iloc[0]})")

    print("\n==== MVP ====")
    players_info["mvp_points"] = ((players_info["totalDamageDealt"] + players_info["totalDamageTaken"] + (players_info["totalMinionsKilled"] * 300) + players_info["damageDealtToTurrets"]) * (players_info["kda"] / 2))
    mvp_player = players_info.sort_values(by="mvp_points", ascending=False).iloc[0][["riotIdGameName", "championName"]]
    print(f"{mvp_player['riotIdGameName']} ({mvp_player['championName']})")


if __name__ == '__main__':
    import requests
    import json
    import os
    import pandas as pd

    API_KEY = "YOUR_API"

    region, subregion = show_menu()
    name, tag = get_name_tag()
    PUUID = get_account_info()

    count = 5
    get_last_matches()
    print_participants_stats()




