from urllib.request import urlopen
from bs4 import BeautifulSoup
html = ("https://www.pythonscraping.com/exercises/exercise1.html")
bs0bj = BeautifulSoup(html.read());
print(bs0bj.h1)
