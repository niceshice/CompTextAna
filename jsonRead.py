import json


def read(doc):
    with open(doc, "r", encoding="utf8") as f:
        output = json.loads(f.read())["text"]
        return output


string = read(r"D:\cravi\Documentsold\Uni\DH\CompTextAna\Korpus\Thriller\13_sins.json")
print(string)
