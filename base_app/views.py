from django.http import request
from django.shortcuts import render,redirect
from django.contrib import messages
from .models import *

# Create your views here.

def MAN_index(request):
    return render(request,"MAN_index.html") 

def MAN_profile(request):
        mem = user_registration.objects.all()
        Num = user_registration.objects.count()
        Man1 = designation.objects.get(designation='Manager')
        Man2 = user_registration.objects.filter(designation = Man1)
        return render(request,'MAN_profile.html',{'Man1':Man2,'num':Num,'mem':mem})  

def MAN_registration(request):
    return render(request,"MAN_registration.html") 
    
def MAN_registrationstaff(request):
    return render(request,"MAN_registrationstaff.html") 
    
def MAN_registrationstudent(request):
    return render(request,"MAN_registrationstudent.html") 

def MAN_currentstaff(request):
    mem = user_registration.objects.all()
    return render(request,"MAN_currentstaff.html",{'mem':mem}) 