import requests
from bs4 import BeautifulSoup
import warnings
import csv
warnings.filterwarnings("ignore")


sub_cities_for_crowling=[]
sub_links_for_crowling=[]
sub_links_for_Featured_Collections=[]
sub_links_for_Featured_Project=[]
data=[["Company Name","Esablished","Total Projects","About Company"],]
data2=[['Company Name','pricing',"Emi",'Project Name','Location',"Config",'Possession Status'],]
data3=[['State Name/Location','pricing',"Emi",'Project Name','Location',"Config",'Possession Status'],]
data4=[['Project Name','Company Name','Project Location','Min. Price per sq.ft.','Configurations','Possession Date','Super Builtup Area'],]
def web(page,WebUrl):
    if(page>0):
        url = WebUrl
        code = requests.get(url)
        plain = code.text
        state_name=url.split("-")
        #print(plain)

        s = BeautifulSoup(plain, "html.parser")
        # print("Featured Projects Link {}".format(state_name[-1]))
        for feat_link in s.findAll('a', {'target': '_blank', 'class': 'css-tb25m1'}):
            tet_2 = feat_link.get('href')
            link = "https://housing.com" + tet_2
            print(link)
            sub_links_for_Featured_Project.append(link)
        # print("Featured Collections Link {}".format(state_name[-1]))
        for feat_link in s.findAll('a', {'target': '_blank', 'class': 'css-12s1udu'}):
            tet_2 = feat_link.get('href')
            link = "https://housing.com" + tet_2
            # print(link)
            sub_links_for_Featured_Collections.append(link)
        # for link in s.findAll('a', {'target':'_blank' ,'class':'css-0'}):
        #     tet_2 = link.get('href')
        #     if  '/in/buy/real-estate-' in tet_2:
        #         link = "https://housing.com" + tet_2
        #         sub_cities_for_crowling.append(link)
                # print(link)
        # print("Featured Developers {}".format(state_name[-1]))
        for divs in s.findAll('div', {'class':'css-1rt9uxw'}):
            for link in divs.findAll('a', {'class':'css-0','target':'_blank'}):
                tet_2 = link.get('href')
                link="https://housing.com"+tet_2
                # print(link)
                sub_links_for_crowling.append(link)



def sub_crowling(weburl):
    url=weburl
    d1=[]
    code = requests.get(url)
    plain = code.text
    s = BeautifulSoup(plain, "html.parser")
    for divs in s.findAll('div', {'class': 'devlpr-title-units'}):
        comp=divs.find('h3',{'class': 'title-h3'})
        comp_name=comp.text
        d1.append(comp_name)
        # for div in divs.findAll('div',{'class': 'gp-title'}):
        #     for x in div:
        #         print(x)
        for div in divs.findAll('div',{'class': 'gp-total'}):
            for x in div:
                d1.append(x)
    for div in s.findAll('div',{'class': 'devlpr-desc'}):
        for d in div:
            d1.append(d.text)
            # for d in div.find('div'):
            #     print(d)
    data.append(d1)
    for divs in s.findAll('div', {'class': 'infi-item-wrapper'}):
        for div in divs.findAll('div', {'class': 'list-item-container'}):
            d2 = []
            for di in div:
                # print(di)
                # print("--------")
                d2.append(comp_name)
                for x in di.findAll('span', {'class': 'lst-price'}):
                    a = BeautifulSoup(str(x))
                    [x.extract() for x in a.findAll('i')]
                    d2.append(a.text)
                for emidiv in di.findAll('div', {'class': 'stub emiWidget'}):
                    a = BeautifulSoup(str(emidiv))
                    [x.extract() for x in a.findAll('i')]
                    d2.append(a.text)
                for div in di.findAll('div',{'class': 'lst-heading project'}):
                    d2.append(div.find('a').contents[0])
                for div in di.findAll('div', {'class': 'lst-loct text-ellipsis'}):
                    d2.append(div.find('a').contents[0])
                for div in di.findAll('div',{'class': 'lst-sub-value lst-config-title text-ellipsis'}):
                    for d in div:
                        d2.append(d)

            data2.append(d2)
def sub_feature_crowling(weburl):
    url = weburl
    print("Working on---->",url)
    code = requests.get(url)
    plain = code.text
    state_name=url.split("-")
    s = BeautifulSoup(plain, "html.parser")
    for divs in s.findAll('div', {'class': 'infi-item-wrapper'}):
        for div in divs.findAll('div', {'class': 'list-item-container'}):
            d2 = []
            for di in div:
                d2.append(state_name[-1])
                # print(di)
                # print("--------")
                for x in di.findAll('span', {'class': 'lst-price'}):
                    a = BeautifulSoup(str(x))
                    [x.extract() for x in a.findAll('i')]
                    d2.append(a.text)
                for emidiv in di.findAll('div', {'class': 'stub emiWidget'}):
                    a = BeautifulSoup(str(emidiv))
                    [x.extract() for x in a.findAll('i')]
                    d2.append(a.text)
                for div in di.findAll('div',{'class': 'lst-heading project'}):
                    d2.append(div.find('a').contents[0])
                for div in di.findAll('div', {'class': 'lst-loct text-ellipsis'}):
                    d2.append(div.find('a').contents[0])
                for div in di.findAll('div',{'class': 'lst-sub-value lst-config-title text-ellipsis'}):
                    for d in div:
                        d2.append(d)

            data3.append(d2)

def sub_feature_Project_crowling(weburl):
    d1=[]
    url = weburl
    print("Working on---->",url)
    code = requests.get(url)
    plain = code.text
    s = BeautifulSoup(plain, "html.parser")
    for div in s.findAll('div',{'class':'head'}):
        d1.append(div.text)
    for div in s.findAll('div', {'class': 'mt-10 txt uc builder-text'}):
        d1.append(div.find('span').text)
    for div in s.findAll('div', {'class': 'location-info grey txt mt-10'}):
        d1.append(div.text)
    l=[]
    for div in s.findAll('section', {'class': 'project-info-container'}):
        quotes = [quote for quote in div.find_all('div', class_='info-value')]
        for i in range(0,len(quotes)):
            if i%2==0:
                l.append(quotes[i])
    for element in l:
        d1.append(element.text)
    data4.append(d1)


url = 'https://housing.com/'
code = requests.get(url)
plain = code.text
with open("housing.txt",'w',encoding="utf-8") as f:
        f.write(plain)
s = BeautifulSoup(plain, "html.parser")
for link in s.findAll('a', {'target':'_blank' ,'class':'css-0'}):
        tet_2 = link.get('href')
        if  '/in/buy/real-estate-' in tet_2:
            link = "https://housing.com" + tet_2
            sub_cities_for_crowling.append(link)
            print(link)


print(len(sub_cities_for_crowling))
print("*******************************************")


for state in sub_cities_for_crowling:
    web(1,state)
print("*******************************************")

for x in sub_links_for_crowling:
    sub_crowling(x)
print("*******************************************")

sub_links_for_Featured_Collections.remove('https://housing.com/in/buy/goa/ready_to_move_projects-goa')
sub_links_for_Featured_Collections.remove('https://housing.com/in/buy/goa/luxury-goa')
sub_links_for_Featured_Collections.remove('https://housing.com/in/buy/goa/value-goa')
sub_links_for_Featured_Collections.remove('https://housing.com/in/buy/mysore/township-mysore')
sub_links_for_Featured_Collections.remove('https://housing.com/in/buy/mysore/value-mysore')
sub_links_for_Featured_Collections.remove('https://housing.com/in/buy/panchkula_haryana/ready_to_move_projects-panchkula_haryana')


for link in sub_links_for_Featured_Collections:
    sub_feature_crowling(link)
print("*******************************************")

for link in sub_links_for_Featured_Project:
    sub_feature_Project_crowling(link)
print("*******************************************")


print(data)
print(data2)
print(data3)
print(data4)
print(len(sub_cities_for_crowling))
print(len(sub_links_for_Featured_Project))
print(len(sub_links_for_Featured_Collections))
print(len(sub_links_for_crowling))

with open('Company_Data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)


with open('Company_Project_india.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data2)


with open('Featured Collections_Project_india.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data3)


with open('feature_Project_india.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data4)
