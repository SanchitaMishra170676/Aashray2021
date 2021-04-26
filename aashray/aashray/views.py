from django.shortcuts import render, redirect 
from django.contrib import messages
from django.template.loader import render_to_string
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from .models import Contact, PlasmaDonorForm

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
        try:
            Name = request.POST.get('name')  
            Age = request.POST.get('age')
            Email = request.POST.get('email')
            Contact = request.POST.get('contact')
            BloodGroup = request.POST.get('bloodGroup')
            Address = request.POST.get('address')
            City = request.POST.get('city')
            Date = request.POST.get('date')
            PrevDonation = request.POST.get('prevDonation')
            Antibodies = request.POST.get('antibodies')
            MedIssues = request.POST.get('medIssues')
            cntc = PlasmaDonorForm.objects.filter(contact = Contact)
            if (len(cntc)):
                messages.error(request,"This entry already exists.")
                return redirect ('donate_plasma')
            plasmaDonorForm = PlasmaDonorForm(name=Name, age= Age, email=Email, contact= Contact, bloodGroup = BloodGroup, address= Address, city=City, date= Date, prevDonation = PrevDonation, antibodies = Antibodies, medIssues = MedIssues)
            plasmaDonorForm.save()
            messages.success(request,'Details Received! We will contact you soon.')
            return redirect ('home')
        except:
            messages.error(request,"Error Occured! Kindly contact the team.")
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