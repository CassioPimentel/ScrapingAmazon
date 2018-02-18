import urllib
from bs4 import BeautifulSoup

url = "https://www.amazon.com.br/Loja-Tudo-Jeff-Bezos-Amazon/dp/8580574897/ref=sr_1_1?ie=UTF8&qid=1518971948&sr=8-1&keywords=loja+de"
pagina = urllib.urlopen(url)
ObjBS = BeautifulSoup(pagina.read())
print(ObjBS.title)

Titulo = ObjBS .findAll("span", {"id": "productTitle"});
Preco = ObjBS .findAll("span", {"class": "a-size-base a-color-price a-color-price"});
Descricao = ObjBS .findAll("div", {"class": "productDescriptionWrapper"});

print Titulo[0].text
print Preco[0].text
print Descricao[0].text
