from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return HttpResponse('Hello, World!')


def add(request, arg_1, arg_2):
    result = arg_1 + arg_2 
    return HttpResponse(result)