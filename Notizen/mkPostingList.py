import os
import collections as col
import re

# get list of files for indices
indexingList = os.listdir(r"./erzaehltexte")
# make defaultdict: added keys get a empty list as default value; could also be a set
indexDict = col.defaultdict(list)

# makes a set of types
def tokenize(text):
    tokens = text.split()
    tokens_strip = [re.sub("\W", "", x) for x in tokens]
    typeset_inner = set(tokens_strip)
    return typeset_inner

# reads previously generated list of types
with open(r"./typen.txt", "r", encoding="utf8") as f:
    helpList = f.read()


for doc in indexingList:
    with open(rf"./erzaehltexte/{doc}", "r", encoding="utf8") as f:
        # returns type list of current document
        docset = tokenize(f.read())
        # iterate current document types
        for item in docset:
            # iterates the type list of all documents in folder
            if item in helpList:
                # appends index of currently iterated doc as value to the currently iterated type in current doc
                indexDict[f"{item}"].append(indexingList.index(doc))

# writes posting list to file
with open(r"./postingList.txt", "w", encoding="utf8") as f:
    f.write(str(indexDict))


print(indexDict)
