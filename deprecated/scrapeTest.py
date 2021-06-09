import requests
import os.path
from bs4 import BeautifulSoup

repoPath = "D:\\cravi\\Documentsold\\Uni\\DH\\CompTextAna\\KorpusAlt\\"
categoryName = "Doku-Drama"

try:
    os.mkdir(os.path.join(repoPath, categoryName))
except OSError as error:
    print(error)


def collectLinks(url):
    response = requests.get(url=url,)
    soup = BeautifulSoup(response.content, "html.parser")
    
    # get all links from categories page
    allLinks = soup.find(id="mw-pages").find_all("a")
    
    # get content for each link
    for link in allLinks:
        # only /wiki/ links
        if link["href"].find("/wiki/") == -1:
            continue
        # concat to full url
        getContent("https://de.wikipedia.org" + link["href"])
    else:
        print("Finished!")

    
def getContent(link):
    response = requests.get(url=link,)
    soup = BeautifulSoup(response.content, "html.parser")
    
    # get title for filename
    title = soup.find(id="firstHeading")
    
    # get text content and prettify
    content = prettifyContent(soup.find(id="mw-content-text"))
    
    # write to file
    outFile = open(os.path.join(repoPath, categoryName, title.text + ".txt"), "w", encoding="utf8")
    outFile.write(content)
    
    outFile.close()
    
    
def prettifyContent(content):
    return content.text
    
# start pulling from this link
collectLinks("https://de.wikipedia.org/wiki/Kategorie:" + categoryName)