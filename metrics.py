import json
import os
import spacy
from tqdm import tqdm

nlp = spacy.load("de_core_news_sm")
repo = "./Korpus"
outcol = {"Splatterfilm": {"amount": 0, "size": 0, "tokens": 0},
          "Roadmovie": {"amount": 0, "size": 0, "tokens": 0},
          "Martial-Arts-Film": {"amount": 0, "size": 0, "tokens": 0},
          "Agentenfilm": {"amount": 0, "size": 0, "tokens": 0},
          "Heimatfilm": {"amount": 0, "size": 0, "tokens": 0},
          "Weihnachtsfilm": {"amount": 0, "size": 0, "tokens": 0},
          "Märchenfilm": {"amount": 0, "size": 0, "tokens": 0},
          "total": {"amount": 0, "size": 0, "tokens": 0}}


def get_amount():
    for file in tqdm(os.listdir(repo), desc="raw amount"):
        with open(rf"./Korpus/{file}", "r", encoding="utf8") as f:
            temp = json.loads(f.read())
            outcol[temp['category']]['amount'] += 1


def get_size():
    for file in tqdm(os.listdir(repo), desc="file size"):
        with open(rf"./Korpus/{file}", "r", encoding="utf8") as f:
            temp = json.loads(f.read())
            outcol[temp['category']]['size'] += os.path.getsize(rf"./Korpus/{file}")


def get_tokens():
    for file in tqdm(os.listdir(repo), desc="token amount"):
        with open(rf"./Korpus/{file}", "r", encoding="utf8") as f:
            temp = json.loads(f.read())
            tokenlist = nlp(temp["text"])
            outcol[temp['category']]['tokens'] += tokenlist.__len__()


def get_total():
    a, s, t = 0, 0, 0
    for item in outcol:
        a += outcol[item]['amount']
        s += outcol[item]['size']
        t += outcol[item]['tokens']
    outcol['total'] = {"amount": a, "size": s, "tokens": t}


get_amount()
get_size()
get_tokens()
get_total()

with open("./data/metrics.json", "w", encoding="utf8") as f:
    f.write(json.dumps(outcol, indent=4))
