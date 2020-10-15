import requests
import requests
from bs4 import BeautifulSoup
import warnings
import csv
warnings.filterwarnings("ignore")
sub_cities_for_crowling=[]

d1=[]
def Rent_section_crowling(weburl):
    url = weburl
    code = requests.get(url)
    plain = code.text
    print("working on------>",url)
    s = BeautifulSoup(plain, "html.parser")
    for divs in s.findAll('div', {'data-q': 'price', 'class': 'css-1u1ld4i'}):
        print(divs.text)
    for a in s.findAll('a', {'data-q': 'title', 'class': 'css-dk6esa'}):
        print(a.text)
    for a in s.findAll('a', {'data-q': 'address', 'class': 'css-1s80dbo'}):
        print(a.text)
    for a in s.findAll('div', {'class': 'css-10v2eo1','data-q':"features"}):
        print(a.contents[0].text)
    for a in s.findAll('div', {'class': 'css-10v2eo1','data-q':"features"}):
        print(a.contents[1].text)

    


url = 'https://housing.com/'
code = requests.get(url)
plain = code.text
with open("housing.txt",'w',encoding="utf-8") as f:
        f.write(plain)
s = BeautifulSoup(plain, "html.parser")
for link in s.findAll('a', {'target':'_blank' ,'class':'css-0'}):
        tet_2 = link.get('href')
        if  '/rent/' in tet_2:
            link = "https://housing.com" + tet_2
            sub_cities_for_crowling.append(link)
            print(link)
for i in range(1,len(sub_cities_for_crowling)):
    Rent_section_crowling(sub_cities_for_crowling[i])