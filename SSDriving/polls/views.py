from django.shortcuts import render, render_to_response
from django.http import HttpResponse
import datetime

# Create your views here.
def index(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)
