from django.conf import settings
if not settings.configured:
    settings.configure()

from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render

def index(request):
    return render(request, 'index.html')

