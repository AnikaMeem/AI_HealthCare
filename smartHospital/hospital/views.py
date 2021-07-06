from django.shortcuts import render

# Create your views here.

def home_page(request):
    return render(request,'hospital/index.html')

def aboutus(request):
    return render(request,'hospital/aboutus.html')

def adminlogin(request):
    return render(request,'hospital/login.html',context={
        "usertype":"Admin",
        "image":"images/admin.png"
        })

def doctorlogin(request):
    return render(request,'hospital/login.html',context={
        "usertype":"Doctor",
        "image":"images/doctor.png"
        })

def patientlogin(request):
    return render(request,'hospital/login.html',context={
        "usertype":"Patient",
        "image":"images/patient.png"
        })

def contactUs(request):
    return render(request,'hospital/contactus.html')
