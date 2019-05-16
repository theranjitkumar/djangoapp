from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    # return HttpResponse("home")
    return render(request, 'index.html', {})
def about(request):
    # return HttpResponse("about")
    return render(request, 'about.html', {}) 
