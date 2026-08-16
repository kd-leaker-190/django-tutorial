from django.urls import path
from website.views import *

app_name = 'website'

urlpatterns = [
    path('http-test', http_test, name='http-test'),
    path('json-test', json_test, name='json-test'),
    path('', index_view, name='home'),
    path('about', about_view, name='about'),
    path('contact', contact_view, name='contact'),
]
