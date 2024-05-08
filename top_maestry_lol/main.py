""""

Check README.md


"""

import requests
import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


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


def get_maestry_info():
    # Get the maestry info
    url = f"https://{subregion}.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-puuid/{PUUID}?api_key={API_KEY}"
    response = requests.get(url)

    # Save maestry info to file
    with open(f"maestry_{name}_{tag}.json", "w") as f:
        json.dump(response.json(), f, indent=4)
        f.close()


def show_maestry_graphs():
    # Take only needed columns
    maestry = pd.read_json(f"maestry_{name}_{tag}.json")[["championId", 'championLevel', "championPoints"]]
    top_maestry = maestry.sort_values(by=['championPoints'], ascending=False)[:5]
    total_maestry = maestry["championPoints"].sum()
    total_top_maestry = top_maestry["championPoints"].sum()

    champions = pd.read_json("all_champions.json")
    # Fixed data column, change key column to int64, and take only 'id', 'key', 'name'
    champions = pd.json_normalize(champions.data)[["id", "key", "name"]].astype({'key': np.int64})

    # Like inner join left championId with key, and take only needed columns
    merged_maestry = pd.merge(top_maestry, champions, left_on="championId", right_on="key", how="left")[["championId", "championLevel", "championPoints", "name"]]

    fig, ax = plt.subplots(1, 2, figsize=(12, 6))

    ax[0].bar(merged_maestry["name"], merged_maestry["championPoints"])

    ax[0].set_ylabel('Points')
    ax[0].set_title('Top 5 Champions Maestry')

    rest_maestry = total_maestry - total_top_maestry
    data = merged_maestry["championPoints"]
    data = data._append(pd.Series(rest_maestry))

    labels = merged_maestry["name"]
    labels = labels._append(pd.Series("Other"))

    ax[1].pie(data, labels=labels, autopct='%1.1f%%')

    plt.show()


if __name__ == "__main__":
    API_KEY = "RGAPI-9d677c97-a2d1-4eb3-88db-e1b4a286deca"

    region, subregion = show_menu()
    name, tag = get_name_tag()
    PUUID = get_account_info()

    get_maestry_info()
    show_maestry_graphs()





