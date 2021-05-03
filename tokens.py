import json
import os
import spacy

repo = r"./Korpus/"
nlp = spacy.load("de_core_news_sm")
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
        tokenlist = nlp(temp["text"])
        outcol[temp['category']] += tokenlist.__len__()


for item in outcol:
    total += outcol[item]


print(outcol, total)
