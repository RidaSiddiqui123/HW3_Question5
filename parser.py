from pymongo import MongoClient
from db_connection_mongo_CS import *
from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup
from urllib.parse import urljoin



url = 'https://www.cpp.edu/sci/computer-science/'
frontier = [url]
visited = []


if __name__ == '__main__':
    # Connecting to the database
    db = connectDataBase()
    # Creating a collection
    pages = db.pages
    professors = db.professors


def crawlerThread(frontier):
    while len(frontier) != 0:
        url = frontier[0]
        visited.append(url)
        html = urlopen(url)
        bs = BeautifulSoup(html.read(), 'html.parser')
        frontier.pop(0)
        #crawler.py
        #slide 21
        information = str(bs.find("html"))
        insertPage(pages, url, information)
        #storePage(url, html) put it into the mongodb database
        if bs.find('h1').get_text() == "Permanent Faculty":
            pageURL = visited[len(visited)-1]
            print(pageURL)
            parsePage(pageURL)
            #getPageURL(pages, page)
            frontier.clear()
            break
        else:
            links = bs.find_all("a")  # Find all elements with the tag <a>
            for link in links:
                href = link.get("href")
                absolute_url = urljoin(url, href)
                frontier.append(absolute_url)

list = []
list1 = []
def parsePage(pageURL):
 #   print()
    print("page")
    print(pageURL)
    pageToParse = pages.find_one({"url": pageURL}, {"_id": 0, "html": 1})
    print(pageToParse)
    htmlToParse = pageToParse['html']
    print(htmlToParse)
  #  # parse through and get faculty info and send it to other method
    bs = BeautifulSoup(htmlToParse, 'html.parser')
    #bs.prettify(formatter=lambda s: s.replace(u'\xa0', ' '))
    #ProfsName = bs.find_all("h2")
    print("hehe")
    profInfo = bs.section.find_all("div", {"class": "clearfix"})

    print("parvmkvm")
    print(profInfo)


    for i in profInfo:
        #i = i.replace(u'\xa0', '')
        if ((i.find("h2") is not None) and (i.find("p") is not None)):
            name = i.h2.get_text() ##this gives me professors name
            info = i.p.get_text() ## this gives me Title: ... Office: ... Phone: ...


            for j in i.p.find_all("strong"):
                titleText = j.get_text()
                if (titleText == "Title:"):
                    print(j.next_sibling.strip())
                if (titleText == "Office:"):
                    print(j.next_sibling.strip())
                if (titleText == "Email:"):
                   print(j.next_sibling.next_sibling.get_text().strip())
                #if (titleText == "Web:"):
                 #   print(j.next_sibling)

            #if "Office" in info:
            #list.append(name.strip())


            #insertFaculty(professors, name, info)

            list1.append(info)
     #use html to get the 'Title stuff an so on


#maybe use hash table
    #print(list)
    print(list1)

    #insertFaculty(professors, list, list1)






    #for child in bs.find('section', {'class': 'text_images'}).children:
     #   print(child)

try:
    crawlerThread(frontier)
    #getPageURL(page)
except HTTPError as e:
    print(e)
except URLError as e:
    print('The server could not be found!')
else:
    print('It Worked!')






























