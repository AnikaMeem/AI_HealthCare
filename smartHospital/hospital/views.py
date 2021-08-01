from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect,HttpResponse
from django.views.generic import DetailView,View
from .models import Doctor,Patient


# Create your views here.

def home_page(request):
    return render(request,'hospital/index.html')

def aboutus(request):
    return render(request,'hospital/aboutus.html')
    

def doctorlogin(request):
    if request.session.get("paientID"):
        return HttpResponseRedirect(reverse("doctorDash"))
    if request.method == "POST":
        email = request.POST["userEmail"]
        password = request.POST["userPassword"]
        doctor = Doctor.objects.get(email=email)        
        if password == doctor.password:
            request.session["doctor"] = f"{doctor.first_name} {doctor.last_name}"
            request.session["doctorID"] = doctor.id
            return HttpResponseRedirect(reverse("doctorDash"))
    return render(request,'hospital/login.html',context={
        "title":"Doctor Login",
        "usertype":"Doctor Email",
        "image":"images/doctor.png"
        })

def patientlogin(request):
    if request.method == "POST":
        email = request.POST["userEmail"]
        password = request.POST["userPassword"]
        patient = Patient.objects.get(email=email)        
        if password == patient.password:
            request.session["patient"] = f"{patient.first_name} {patient.last_name}"
            request.session["paientID"] = patient.id
            print(request.session["patient"],request.session["paientID"])
    # 'hospital/login.html'
    return render(request,'hospital/patient_dash.html',context={
        "title":"Patitent Login",
        "usertype":"Patient Email",
        "image":"images/patient.png"
        })

def contactUs(request):
    return render(request,'hospital/contactus.html')

class DoctorDash(View):
    def get(self,request):
        if request.session.get("doctorID"):
            doctor = Doctor.objects.get(pk = request.session["doctorID"])
            return render(request,"hospital/doctor_dash.html",context={
                "doctor" : doctor
            })
        else:
            return HttpResponseRedirect(reverse("doctorlogin"))
    def post(self,request):
        if request.POST["logout"]:
            del request.session["doctor"]
            del request.session["doctorID"]
            return HttpResponseRedirect(reverse("homepage"))


def diseasePrediction(request):
    return HttpResponse("Hello World")