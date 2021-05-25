import json
import os
from tqdm import tqdm

repo = "./Korpus/"
out = set()

for doc in tqdm(os.listdir("./BoWs/")):
    with open(f"./BoWs/{doc}", "r", encoding="utf8") as f:
        words = json.loads(f.read())
        for word in words:
            out.add(word)

outlist = []
outlist.extend(out)
outlist.sort()

with open("./data/lemmata.json", "w", encoding="utf8") as f:
    f.write(json.dumps(outlist))
