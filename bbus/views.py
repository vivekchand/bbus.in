from django.conf import settings
if not settings.configured:
    settings.configure()
import json
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
import requests
from lxml import html
from BeautifulSoup import BeautifulSoup
from bbus_utils import *

def index(request):
    return render(request, 'index.html')

def search(request):
    src = request.POST.get('from')
    dst = request.POST.get('to')
    how = request.POST.get('how')
    page = requests.post(settings.DATA_URL,
        data={'from': src, 'to': dst, 'how': how})
    soup = BeautifulSoup(page.text)
    tables = soup.findAll('table')
    bus_routes = []
    routes = 0
    for table in tables:
        routes += 1
        bus_routes.append(table2json(table.findAll('tr')))
    return render(request, 'search.html', {'routes':bus_routes})
