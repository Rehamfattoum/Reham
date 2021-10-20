from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index (request):
    return HttpResponse("Hello world !!")

def Reham (request):
    return HttpResponse("Hello reham !!")

def Rita (request):
    return HttpResponse("Hello rita !!")
def greet (request,name):
    return HttpResponse (f"Hello,{name}!".title())