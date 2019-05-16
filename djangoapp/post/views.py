from django.shortcuts import render
from django.http import HttpResponse
import json

x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON:
posts = json.dumps(x)


def post(request):
    # return HttpResponse("post")
    # posts = Post.objects.all();
    return render(request, 'post.html', {'posts': posts})

def postDetails(request):
    # return HttpResponse("postDetails")
    return render(request, 'details.html', {})

