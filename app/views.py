from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.http import *

def Jampandu(request):
    return HttpResponse('<h1><marquee> Hi Jampandu : How are You</marquee></h1>')

def Jiglerani(request):
    return HttpResponse('<h1><marquee> Hi Jiglerani : How are You</marquee></h1>')


