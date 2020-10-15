import requests
from bs4 import BeautifulSoup
import csv
def web(page,WebUrl):
    data=[["Mobile/Assoseries Title","Mobile/Assoseries Url"],]
    if(page>0):
        url = WebUrl
        code = requests.get(url)
        plain = code.text
        with open("amazon.txt",'w',encoding="utf-8") as f:
            f.write(plain)
        s = BeautifulSoup(plain, "html.parser")
        print(s)
        for link in s.findAll('a', {'class':'s-access-detail-page'}):
            d1 = []
            tet = link.get('title')
            d1.append(tet)
            tet_2 = link.get('href')
            d1.append(tet_2)
        data.append(d1)
        with open('Amazon Data.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(data)
web(1,'https://www.amazon.in/gp/browse.html?node=1389401031&ref_=nav_em_T1_0_4_NaN_1_sbc_mobcomp_all_mobiles')