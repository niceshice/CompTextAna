import json
import os
import re
from tqdm import tqdm

repo = "./Korpus/"

with open(f"./data/lemmata.json", "r", encoding="utf8") as lf:
    lem = json.loads(lf.read())
    lemdict = dict()

    for doc in tqdm(os.listdir(repo)):

        for i in lem:
            lemdict[i] = 0

        with open(f"{repo}{doc}", "r", encoding="utf8") as f:
            tokenlist = re.findall("\w+", f.read().lower())
            tokenset = set(tokenlist)

            for token in tokenset:
                lemdict[token] = tokenlist.count(token)

            with open(f"./Dokumentvektoren/{doc}", "w", encoding="utf8") as out:
                out.write(json.dumps(list(lemdict.values())))

        lemdict.clear()
