import json
import os

repo = r"./Korpus/"
temp = ""
total = 0

outcol = {"Splatterfilm": 0,
          "Roadmovie": 0,
          "Martial-Arts-Film": 0,
          "Agentenfilm": 0,
          "Heimatfilm": 0,
          "Weihnachtsfilm": 0,
          "Märchenfilm": 0}


for file in os.listdir(repo):
    with open(rf"./Korpus/{file}", "r", encoding="utf8") as f:
        temp = json.loads(f.read())
        outcol[temp['category']] += 1


for item in outcol:
    total += outcol[item]


print(outcol, total)
