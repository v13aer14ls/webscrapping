#Esse scrapper aqui ignora uns erros e coisa e talz

#Importa as libs necessárias pro scrapper rodar
from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

#Verifica o codigo HTTP
def getTitle():
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
#Verifica se o Atributo ou Objeto existe
    try:
        bs0bj = BeautifulSoup(html.read())
        title = bs0bj.body.h1
    except AttributeError as e:
        return None
    return title
#Verifica se tem conteúdo
title = getTitle("https://www.pythonscraping.com/exercises/exercise1.html")
if title == None:
    print ('Title could not be found !')
else:
    print(title)


#Só deus sabe porque o erro tá rolando 
