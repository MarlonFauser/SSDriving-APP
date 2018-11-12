from django.shortcuts import render, render_to_response
from django.http import HttpResponse
import datetime

# Create your views here.
def index(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % 1)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % 1)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % 1)