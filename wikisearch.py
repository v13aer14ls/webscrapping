'''
Uma função individual que o getLinks recebe um URL de artigo da wikipedia na forma /wiki/nomedoartigo e retorna ua lista de todos URLS de artigos vinculados,com o mesmo formato

Uma função principal que chame getLinks com algum artigo inicial, selecione um link de artigo aleatorio na lista retornada e chame GetLinks novamente até que não sejam encontrados links de artigo na nova página.
'''


from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import random
import re
random.seed(datetime.datetime.now())
def getLinks(articleUrl):
    html = urlopen("http://en.wikipedia.org"+articleUrl)
    bs0bj = BeautifulSoup(html)
    return bs0bj.find("div", {"id":"bodyContent"}).findAll("a",href=re.compile("^(/wiki/)((?!:).)*$"))
links = getLinks("/wiki/Kevin_Bacon")
while len(links) > 0:
    newArticle = links[random.randint(0,len(links)-1)].attrs["href"]
    print(newArticle)
    links = getLinks(newArticle)
