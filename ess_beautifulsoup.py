from bs4 import BeautifulSoup
import urllib.request

url = "http://www.pythonforbeginners.com"
#url = "http://www.pythonforbeginners.com"
page = urllib.request.urlopen(url).read() 

soup = BeautifulSoup(page)
'''
print(soup.prettify())
print("Title: ")
print(soup.title)

print("Title string: ")
print(soup.title.string)

import re
for tag in soup.find_all(re.compile("^b")):
    print(tag.name)

for tag in soup.find_all(True):
    print(tag.name)

print(soup.a)
print(soup.body)


for tag in soup.find_all(['a','div']): #find a and div
    print(tag)
    
print('>>>>>>')
'''
for tag in soup.find_all('div',{'class':'categories'}): #find all <div> with cluss=cutegories
    print(tag)
    
print('>>>>>>>>>>>>>')

for tag in soup.find_all('div',{'class':'categories','id':'fb-root'}): #applies AND to specs in dictionary and find nothing
    print(tag)
    
print('>>>>>>>>>>>>>')
    
for tag in soup.find_all('div',{'id':'fb-root'}): #find the <div> with id=fb-root
    print(tag)

tag = soup.find(id='fb-root')
print(tag)

