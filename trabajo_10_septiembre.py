import csv

def bubble_sort(arr, key):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j][key] < arr[j + 1][key]:  
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

games = []

with open("games.csv", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
    
        row["PTS_home"] = float(row["PTS_home"]) if row["PTS_home"] != "" else 0.0
        row["PTS_away"] = float(row["PTS_away"]) if row["PTS_away"] != "" else 0.0
        row["TOTAL_POINTS"] = row["PTS_home"] + row["PTS_away"]
        games.append(row)

sorted_games = bubble_sort(games, "TOTAL_POINTS")

for g in sorted_games[:10]:
    print(
        g["GAME_DATE_EST"],
        g["HOME_TEAM_ID"], g["PTS_home"], "-",
        g["VISITOR_TEAM_ID"], g["PTS_away"],
        "Total:", g["TOTAL_POINTS"]
    )
