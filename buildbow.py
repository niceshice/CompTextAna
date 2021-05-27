import json

from tqdm import tqdm

tempdict = dict()
with open("./data/lemmata.json", "r", encoding="utf8")as f:
    templ = json.loads(f.read())
    for item in tqdm(templ):
        tempdict[item] = templ.index(item)

    with open("./data/lemmataDICT.json", "w", encoding="utf8")as f:
        f.write(json.dumps(tempdict, indent=2))