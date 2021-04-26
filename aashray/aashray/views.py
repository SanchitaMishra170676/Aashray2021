from django.shortcuts import render, redirect 
from django.contrib import messages
from django.template.loader import render_to_string
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from .models import Contact

def home(request):
    if request.method =='POST':
        Name = request.POST.get('name')  
        Message = request.POST.get('message')
        Subject = request.POST.get('subject') 
        Email = request.POST.get('email')
        contact = Contact(name=Name, message=Message, subject=Subject, email=Email)
        contact.save()
        messages.success(request,'Message received! Thank you for cntacting us.')
        return redirect ('home')
    return render(request,'index.html')

def donate_plasma(request):
    if request.method =='POST':
        Name = request.POST.get('name')  
        Message = request.POST.get('message')
        Subject = request.POST.get('subject') 
        Email = request.POST.get('email')
        contact = Contact(name=Name, message=Message, subject=Subject, email=Email)
        contact.save()
        messages.success(request,'Message received! Thank you for cntacting us.')
        return redirect ('home')
    return render(request,'donor.html')  

def hospital_beds(request):
    return render(request,'beds1.html')   

def hospital_beds_data(request):
    return render(request,'beds2.html') 

def medicines(request):
    return render(request,'medicines1.html') 

def medicines_data(request):
    return render(request,'medicines2.html') 

def oxygen(request):
    return render(request,'oxygen1.html')  

def oxygen_data(request):
    return render(request,'oxygen2.html')     

def plasma(request):
    return render(request,'plasma1.html')  

def plasma_data(request):
    return render(request,'plasma2.html') 

def helplines(request):
    return render(request,'helplines.html')  

def others(request):
    return render(request,'others.html')                           