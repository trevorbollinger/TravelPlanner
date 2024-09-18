import requests
from django.shortcuts import render
from .api_calls import *

def hello_view(request):
    return render(request, 'hello.html')
