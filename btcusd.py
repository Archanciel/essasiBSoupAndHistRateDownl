from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

def cleanRate(rateStr):
    '''
    remove thousands divider from passed 
    rate string and return cleaned string
    '''
    return rateStr.replace(',','')
    
url = "https://bitinfocharts.com/markets/kraken/btc-usd-all.html"
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'}) 
page = urlopen(req).read()

soup = BeautifulSoup(page)
#print(soup.prettify())

spanLastTrade = soup.find(id='lastTrade')
spanPrice = spanLastTrade.find('span',{'itemprop':'price'})
print(cleanRate(spanPrice.string))


