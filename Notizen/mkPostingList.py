import os
import collections as col
import re

indexingList = os.listdir(r"./erzaehltexte")
indexDict = col.defaultdict(list)


def tokenize(text):
    tokens = text.split()
    tokens_strip = [re.sub("\W", "", x) for x in tokens]
    typeset_inner = set(tokens_strip)
    return typeset_inner


with open(r"./typen.txt", "r", encoding="utf8") as f:
    helpList = f.read()


for doc in indexingList:
    with open(rf"./erzaehltexte/{doc}", "r", encoding="utf8") as f:
        docset = tokenize(f.read())
        for item in docset:
            if item in helpList:
                indexDict[f"{item}"].append(indexingList.index(doc))


with open(r"./postingList.txt", "w", encoding="utf8") as f:
    f.write(str(indexDict))


print(indexDict)
