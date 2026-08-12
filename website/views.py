from django.http import HttpResponse, JsonResponse

def http_test(req):
    return HttpResponse('<h1>This is a Http Test</h1>')

def json_test(req):
    return JsonResponse({ 'message': 'This is a json test url' })

def index_view(req):
    return HttpResponse('<h1>Home page</h1>')

def about_view(req):
    return HttpResponse('<h1>About page</h1>')

def contact_view(req):
    return HttpResponse('<h1>Contact page</h1>')
