import urllib
from urllib.request import urlopen
from bs4 import BeautifulSoup

myurl = "https://top5ofanything.com/list/b6527cf2/Largest-Volcanic-Islands"
markup = urllib.request.urlopen(myurl)
soup = BeautifulSoup(markup, "lxml")

# find all tables
table = soup.find("table")
# find only one table
# tables = soup.find("table")

print(soup.title)

for row in table:
    for el in row:
        print(el.get_text(" "))
