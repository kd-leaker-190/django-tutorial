from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

def blog_view(req):
    return render(req, 'blog/index.html')

def blog_single(req):
    return render(req, 'blog/single.html')
