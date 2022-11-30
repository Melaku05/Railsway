from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1 style='text-align:center; height:100%; background:pink'>Hello, world. You're at the polls index.</h1>")

# Create your views here.
