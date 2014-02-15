from django.conf import settings
if not settings.configured:
    settings.configure()
import json
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render

def index(request):
    return render(request, 'index.html')

def bbus_list(request):
    bus_json = open(settings.BASE_DIR+'/bbus/bus_json.json').read().split('\n')
    return HttpResponse(json.dumps(bus_json), content_type="application/json")
    
