import os
import json
import spacy
from tqdm import tqdm

repo = "./Testkorpus/"
nlp = spacy.load("de_core_news_sm")
lemmas = set()

for doc in tqdm(os.listdir(repo)):
    with open(f"{repo}{doc}", "r", encoding="utf8") as f:
        tempdict = json.loads(f.read())
        text = nlp(tempdict["text"])
        for word in text:
            lemmas.add(word.lemma_)

    with open(f"./BoWs/{doc}.json", "w", encoding="utf8") as f:
        f.write(str(lemmas))


