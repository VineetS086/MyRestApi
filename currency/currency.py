from bs4 import BeautifulSoup
from django.db.models import query
import requests, json, time

from .models import Currency

c1 = 'INR'

def convert(c2 = 'inr'):
    a1 = 1000
    c2 = c2.upper()

    if c1==c2:
        return 1.0, c1

    url     = 'https://www.google.co.in/search?q='+str(a1)+'+'+c2+'+to+'+c1+'' 
    agent   = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'

    headers = {'User-Agent':agent}

    x = requests.get(url,headers = headers)
    soup = BeautifulSoup(x.content, 'html.parser')
    
    curr_tag    = soup.find("span", {"class": "DFlfde SwHCTb"})
    curr_val    = float(curr_tag['data-value'])/a1
    curr_name   = soup.find("span", {"class": "vLqKYe"})['data-name']

    return curr_val, curr_name

def update(code):
    curr = Currency.objects.get(code=code)

    if code==c1:
        curr.save()
        return
    try:
        amount, name    = convert(code)
    
        curr.value      = amount
        curr.name       = name
        curr.update_status = True
    except:
        curr.update_status = False

    curr.save()

def update_all():
    query_set = Currency.objects.all()
    for curr in query_set:
        update(curr.code)
    
def rain_check():
        
    with open('file.json', 'r') as fhand:
        #data    = fhand.read()
        data    = json.load(fhand)
    
    time_now = time.time()
    if time_now-data['time']>data['time limit']:
        update_all()
        print('Updated Currency Values to the database')
        data['time']=time_now
        data['noted_time']=time.ctime()
        
        data['currency']['updates']+=1
        data['total updates']+=1

    data['currency']['count']=len(Currency.objects.all())
    
    with open('file.json', 'w') as fhand:
        json.dump(data, fhand, indent = 4)

