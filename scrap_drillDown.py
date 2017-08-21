from bs4 import BeautifulSoup
import urllib.request

url ='http://en.wikipedia.org/wiki/List_of_A_Song_of_Ice_and_Fire_characters' 
page = urllib.request.urlopen(url).read() 

soup = BeautifulSoup(page)
#Create a variable to score the scraped data in 
character_name = []

# for each item in all the toclevel-2 li items # (except the last three because they are not character names), 
for item in soup.find_all('li',{'class':'toclevel-2'})[:-3]: # find each span with class=toctext, 
    for post in item.find_all('span',{'class':'toctext'}): # add the stripped string of each to character_name, one by one 
        character_name.append(post.string.strip())

for name in character_name:
    print(name)