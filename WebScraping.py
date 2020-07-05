import requests
from bs4 import BeautifulSoup
import pandas as pd

URL = 'https://es.wikipedia.org/wiki/Anexo:Pa%C3%ADses_y_territorios_dependientes_por_poblaci%C3%B3n'
URL2 = 'https://es.wikipedia.org/wiki/Anexo:Pa%C3%ADses_por_continentes'
page = requests.get(URL)
page2 = requests.get(URL2)
soup = BeautifulSoup(page.content,'html.parser')
soup2 = BeautifulSoup(page2.content,'html.parser')

#Copiando paises
td_paises = soup.table.tbody.find_all('td')
td_search = list(td_paises)

Pais = list()
for i in range(1,2920,12):
    Pais.append(td_search[i].find('a').text)


#Copiando cantidad de habitantes
contenido = soup.table.find('tbody')
tr = contenido.find_all('tr')

numHabitantes = list()
for i in range(1,245):
    search = tr[i].find('td',text=f"{i}")
    iterable_hermanos = search.find_next_siblings('td')
    lista = list(iterable_hermanos)
    aux = lista[7].text.split()
    index = 0
    for z in aux:
        if z == " ":
            aux.pop(index)
            index += 1
        index += 1    
    nHab = "".join(aux)
    numHabitantes.append(nHab)

#Preparando lista de continentes
continentes_iterable = soup2.body.find('div', class_="mw-parser-output")
continentes = continentes_iterable.find_all('table')

#Copiando paises Europa
search = continentes[1].find_all('td',align="center")
print("====================PAISES EUROPA====================")
count = 0
for i in search:
    print(i.contents[2].text,end="\n\n")
    count += 1
print(f"Europa tiene {count} paises\n\n\n")

#Copiando paises de Asia
search = continentes[3].find_all('td',align="center")
print("====================PAISES ASIA====================")
count = 0
for i in search:
    print(i.contents[2].text,end="\n\n")
    count += 1
print(f"Asia tiene {count} paises\n\n\n")

#Copiando paises de Africa
search = continentes[7].find_all('tr')

print("====================PAISES AFRICA====================")
count = 0
index = 0
for i in search:
    if index == 0:
        index += 1
        continue
    else:
        show = i.find('td').find_all('a')
        print(show[0].text,end="\n\n")
        count += 1
print(f"Africa tiene {count} paises\n\n\n")

#Copiando paises de America
search = continentes[8].find_all('td',align="center")
print("====================PAISES AMERICA====================")
count = 0
for i in search:
    print(i.contents[2].text,end="\n\n")
    count += 1
print(f"America tiene {count} paises\n\n\n")




#df = pd.DataFrame({'Paises':Pais, 'Cantidad de habitantes':numHabitantes}, index=list(range(1,245)))
#df.to_csv('Paises.csv', index=False)
