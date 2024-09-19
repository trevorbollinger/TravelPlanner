import requests
from django.shortcuts import render
from .api_calls import *

def hello_view(request):
    return render(request, 'hello.html')

def api_demo_view(request):
    hotel_data = get_hotels()
    attr_data = get_attrs()
    return render(request, 'api_demo.html', {'hotel_data': hotel_data, 'attr_data': attr_data})
