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
    return render(request,'donor.html')  