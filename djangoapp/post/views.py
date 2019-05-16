from django.shortcuts import render

from django.http import HttpResponse


def post(request):
    # return HttpResponse("post")
    return render(request, 'post.html', {})

def postDetails(request):
    # return HttpResponse("postDetails")
    return render(request, 'details.html', {})

