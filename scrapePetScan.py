import requests
import os.path
import re
import json
from datetime import datetime
# from pathlib import Path
from bs4 import BeautifulSoup

repoPath = r"./Korpus/"
# input for dynamic category search
categoryName = input("gib Kategorie: ")

# try:
#     os.mkdir(os.path.join(repoPath, categoryName))
# except OSError as error:
#     print(error)

# notes: identifiers += filenames, join via db


def collectLinks(url):
    response = requests.get(url=url, )
    soup = BeautifulSoup(response.content, "html.parser")

    # get all links from categories table
    all_links = soup.find(id="main_table").find_all("a")

    # get content for each link
    for link in all_links:
        # only /wiki/ links
        if link["href"].find("/wiki/") == -1:
            continue
        # pull content from href-attribute
        getContent(link["href"])
    else:
        print("Finished!")


def getContent(link):
    response = requests.get(url=link, )
    soup = BeautifulSoup(response.content, "html.parser")

    # get title
    title = soup.find(id="firstHeading")
    # format for filename
    title_f = formatTitle(soup.find(id="firstHeading"))
    # TODO: remove, only for logging
    print(title_f)

    if title_f not in os.listdir(repoPath):
        # get text content and prettify
        content = makeJSON(soup.find(id="mw-content-text"), link, title.text)

        # write to file
        with open(os.path.join(repoPath, title_f + ".json"), "w", encoding="utf8") as out_file:
            out_file.write(content)


def makeJSON(content, link, title):
    # make dict with scrape datetime, source(link), title, category and text content
    # TODO add metadata from wikidata
    outdict = {"date": datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
               "link": link,
               "title": title,
               "category": categoryName,
               "text": filterTextOnly(content)
               }
    return json.dumps(outdict, indent=4)


def filterTextOnly(content):
    out_s = ""
    # list all tags <p>
    out_l = content.find_all("p")
    for item in out_l:
        out_s = out_s + item.text
    out_s = re.sub(r"\[.+]", "", out_s)             # filter all annotations
    return out_s


def formatTitle(title):
    title = title.text.casefold()
    title = re.sub(r'[<>:?"/\\|*]', "!", title)
    title = re.sub(r'\s', '_', title)
    return title


# start pulling from this link
collectLinks("https://petscan.wmflabs.org/?ns[0]=1&ns[100]=1&project=wikipedia&categories="
             + categoryName +
             "&depth=10&language=de&ns[6]=1&sortby=ns_title&interface_language=de&ns[10]=1&doit=&interface_language=de")
