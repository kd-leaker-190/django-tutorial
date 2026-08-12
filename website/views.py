from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

def http_test(req):
    return HttpResponse('<h1>This is a Http Test</h1>')

def json_test(req):
    return JsonResponse({ 'message': 'This is a json test url' })

def index_view(req):
    return render(req, 'home/index.html')

def about_view(req):
    return render(req, 'home/about.html')

def contact_view(req):
    return render(req, 'home/contact.html')
