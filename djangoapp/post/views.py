from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
import json

posts = [
	{
	  "pid": "1",
	  "title": "post title",
	  "body": "lorem text....."
	},
	{
	  "pid": "2",
	  "title": "post title",
	  "body": "lorem text....."
	},
	{
	  "pid": "3",
	  "title": "post title",
	  "body": "lorem text....."
	},
]

def post(request):
    # return HttpResponse('posts')
    # posts = Post.objects.all();
    return render(request, 'post.html', {'posts': posts})
def postRestData(request):
	# posts = Post.objects.all();
    return HttpResponse(json.dumps(posts), content_type='application/json')

def postDetails(request):
    # return HttpResponse("postDetails")
    return render(request, 'details.html', {})

