from django.shortcuts import render

from django.http import HttpResponse


def post(request):
    return HttpResponse("post")

def postById(request):
    return HttpResponse("postById")

