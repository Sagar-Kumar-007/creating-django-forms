from django.shortcuts import render
from django.http import HttpResponse
from .forms import create
from .models import StoreData
# Create your views here.

def home(request):
    forms=create()
    return render(request,'home.html',{"forms":forms})

def final(request):
    if request.method=="POST":
        name=request.POST['name']
        roll=request.POST['roll']
        branch=request.POST['branch']
        email=request.POST['email']
        phone=request.POST['phone']
        data=StoreData(name=name, roll=roll,branch=branch,email=email,phone=phone)
        data.save()
        return render(request,'final.html',{"name":name,"roll":roll})
