# Last Matches LOL
You need to change API_KEY to your own (https://developer.riotgames.com/)

If you want more matches just change the count variable value.

You can enter data every time (default) or just assign static values.

## Requirements
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install required libraries

```bash
pip install -r requirements.txt
```

## Output

```text
==== Did you win? ====
+ You won the match

==== TEAM 1 ====
Total barons: 0
Total dragons: 0
Total gold earned: 111629
Total turrets: 0
-------------------------------------------------
8/6/4 (2.0) - Mologinek (Sylas) 
5/4/16 (5.25) - ZzKr (Senna) 
15/5/4 (3.8) - R1pstars (FiddleSticks) 
4/7/8 (1.71) - ThanosTheMadMan (Ezreal) 
12/3/9 (7.0) - Weak Side Bot (Ahri) 
8/7/7 (2.14) - 6933369 (Udyr) 
9/6/12 (3.5) - championdiff (Camille) 
7/5/8 (3.0) - masza Kanna (Lux) 

==== TEAM 2 ====
Total barons: 0
Total dragons: 0
Total gold earned: 66003
Total turrets: 0
-------------------------------------------------
3/8/4 (0.88) - Docisk Spust (Vayne) 
2/8/6 (1.0) - Fane1129 (Warwick) 
6/5/2 (1.6) - me feed PEPEGA (Garen) 
1/7/1 (0.29) - Elox (Yasuo) 
1/6/1 (0.33) - Slazinsky (Garen) 
5/5/2 (1.4) - Childe Predatoir (Trundle) 
3/7/5 (1.14) - Wózk0wy z Płocka (Galio) 
5/7/3 (1.14) - Rah Ami (Gragas) 

==== FIRST BLOOD ====
Mologinek (Sylas)

==== MVP ====
ZzKr (Senna)
```

### Used
- [requests](https://requests.readthedocs.io/en/latest/)
- [json](https://docs.python.org/3/library/json.html)
- [pandas](https://pandas.pydata.org/)
- [Riot APIs](https://developer.riotgames.com/apis)