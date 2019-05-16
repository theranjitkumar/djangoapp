from django.shortcuts import render
from django.http import HttpResponse
import datetime

def index(request):
    # return HttpResponse("home")
    now = datetime.datetime.now()
    return render(request, 'index.html', {'current_date': now})
def about(request):
    # return HttpResponse("about")
    return render(request, 'about.html', {}) 
