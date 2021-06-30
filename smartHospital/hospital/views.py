from django.shortcuts import render

# Create your views here.

def home_page(request):
    return render(request,'hospital/index.html')

def aboutus(request):
    return render(request,'hospital/aboutus.html')

def adminlogin(request):
    return render(request,'hospital/login.html',context={"usertype":"Admin"})

def doctorlogin(request):
    return render(request,'hospital/login.html',context={"usertype":"Doctor"})

def patientlogin(request):
    return render(request,'hospital/login.html',context={"usertype":"Patient"})
