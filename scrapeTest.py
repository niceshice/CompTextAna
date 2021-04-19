import requests
import os.path
from bs4 import BeautifulSoup

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
    
    # get title and content
    title = soup.find(id="firstHeading")
    content = soup.find(id="mw-content-text")
    
    # write to file
    outFile = open(os.path.join("D:\\cravi\\Documentsold\\Uni\\DH\\CompTextAna\\Korpus\\" + title.text + ".txt"), "x", encoding="utf8")
    outFile.write(content.text)
    
    outFile.close()
    

collectLinks("https://de.wikipedia.org/wiki/Kategorie:Psychodrama")