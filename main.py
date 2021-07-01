import requests
from bs4 import BeautifulSoup as beautiful_soup

url = "https://www.webnovel.com/book/monarch-of-time_17766698905784705/chapter-10-the-shameless-lin-family_47781953381914779"
html = requests.get(url)
content = html.content
soup = beautiful_soup(content, "html.parser")

titulo_capitulo = soup.find("h3" ,class_="dib mb0")
cuerpo_capitulo = soup.find_all("div", class_ = "dib pr")


print('----RT:TITULO' + titulo_capitulo.text)

for cuerpo_capitulo_formateado in cuerpo_capitulo:
    print(cuerpo_capitulo_formateado.text)
