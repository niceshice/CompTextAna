import requests
import os.path
import re
# from pathlib import Path
from bs4 import BeautifulSoup

repoPath = "D:\\cravi\\Documentsold\\Uni\\DH\\CompTextAna\\Testkorpus\\"
categoryName = input("Name der gewünschten Kategorie: ")

try:
    os.mkdir(os.path.join(repoPath, categoryName))
except OSError as error:
    print(error)


def collectLinks(url):
    response = requests.get(url=url,)
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
    response = requests.get(url=link,)
    soup = BeautifulSoup(response.content, "html.parser")
    
    # get title for filename
    title = formatTitle(soup.find(id="firstHeading"))
    print(type(title), title)
    
    # get text content and prettify
    content = prettifyContent(soup.find(id="mw-content-text"))
    
    # write to file
    with open(os.path.join(repoPath, categoryName, title + ".txt"), "w", encoding="utf8") as out_file:
        out_file.write(content)
    

def prettifyContent(content):
    return content.text


def formatTitle(title):
    title = re.sub(r'[<>:?"/\\|*]', "!", title.text)
    return title


# start pulling from this link
collectLinks("https://petscan.wmflabs.org/?ns[0]=1&ns[100]=1&project=wikipedia&categories="
             + categoryName +
             "&depth=10&language=de&ns[6]=1&sortby=ns_title&interface_language=de&ns[10]=1&doit=&interface_language=de")
