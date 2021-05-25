import os
import json
import spacy
from tqdm import tqdm

repo = "./Korpus/"
#repo = "./Testkorpus/Test/"
bow_repo = "./BoWs/"
#bow_repo = "./Testkorpus/BoW/"
nlp = spacy.load("de_core_news_sm")

for doc in tqdm(os.listdir(repo)):
    lemmas = set()
    with open(f"{repo}{doc}", "r", encoding="utf8") as f:
        tempdict = json.loads(f.read())
        text = nlp(tempdict["text"])
        for word in text:
            lemmas.add(word.lemma_)

    with open(f"{bow_repo}{doc}", "w", encoding="utf8") as f:
        f.write(json.dumps(list(lemmas)))
