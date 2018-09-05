from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
bs0bj = BeautifulSoup(html)

#Usando find all para extrair uma lista de nomes próprios encontrados selecionando apenas o texto existente nas tags

nameList = bs0bj.findAll("span", {"class":"green"})
for name in nameList:
    print(name.get_text())
