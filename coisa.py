from urllib.request import urlopen

html = urlopen("https://portal.globalweb.com.br/#!/_login")
print(html.read())
