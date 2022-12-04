from django.shortcuts import render
from django.http import HttpResponse

# Create yor views here.


def home(request):
    return HttpResponse('Hello')
