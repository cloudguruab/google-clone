from django.shortcuts import render
from django.http import request, HttpResponse
import requests
from bs4 import BeautifulSoup as bs

# Create your views here.
def index(request):
    return render(request, 'index.html')

def search(request):
    if request.method == 'POST':
        search = request.POST['search']
        # use ask.com to scrape since googlt doesnt 
        # alllow it. 
        url = 'https://www.ask.com/web?q='+str(search) # want to f string this
        res = requests.get(url)
        soup = bs(res.text, 'lxml')
        result_listing = soup.find_all('div', {'class': 'PartialSearchResults-item'})
        final_result = []
        for result in result_listing:
            result_title = result.find(class_='PartialSearchResults-item-title').text
            result_url = result.find('a').get('href')
            result_description = result.find(class_='PartialSearchResults-item-details').text
            
            final_result.append((result_title, result_url, result_description))

        context = {
            'final_result': final_result,
        }

        return render(request, 'search.html', context)
    else:
        return render(request, 'search.html')