from django.shortcuts import render
from django.http import HttpResponse 
import datetime 
# Create your views here.
def index (request):
    return HttpResponse ("hello world !!")
# def vname (request,name):
#     return HttpResponse(f"Hello,{name}")
def chrismas (request):
    now= datetime.datetime.now()
    return render (request,'index.html',{
        "newyear":now.year==1 and now.day==1
    })
def Birth (request,number):
    age=datetime.datetime.now()
    return render (request,'index.html',{
    "old": age.year-number 
    })