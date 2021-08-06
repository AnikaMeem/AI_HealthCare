from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect,HttpResponse
from django.views.generic import DetailView,View
from .models import Doctor,Patient,Appoinment
from .forms import AppoinmentsForm

# Create your views here.

def home_page(request):
    return render(request,'hospital/index.html')

def aboutus(request):
    return render(request,'hospital/aboutus.html')




#############################
#                           #
#    Doctors Views          #
#                           #
#############################

def doctorlogin(request):
    if request.session.get("doctorID"):
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



#############################
#                           #
#    End of Patient Views   #
#                           #
#############################






#############################
#                           #
#    Patient Views          #
#                           #
#############################

class PatientLogin(View):
    def get(self,request):
        if request.session.get("patientID"):
            return HttpResponseRedirect(reverse("patientDash"))
        return render(request,'hospital/login.html',context={
            "title":"Patitent Login",
            "usertype":"Patient Email",
            "image":"images/patient.png"
            })
    def post(self,request):
        email = request.POST["userEmail"]
        password = request.POST["userPassword"]
        patient = Patient.objects.get(email=email)        
        if password == patient.password:
            request.session["patient"] = f"{patient.first_name} {patient.last_name}"
            request.session["patientID"] = patient.id
            return HttpResponseRedirect(reverse('patientDash'))



class PatientDash(View):
    def get(self,request):
        if request.session.get("patientID"):
            patient = Patient.objects.get(pk = request.session["patientID"])
            return render(request,"hospital/patient_dash.html",context={
                "patient" : patient
            })
        else:
            return HttpResponseRedirect(reverse("patientlogin"))
    def post(self,request):
            del request.session["patient"]
            del request.session["patientID"]
            return HttpResponseRedirect(reverse("homepage"))




class Appoinments(View):
    def get(self,request):
        doctors = Doctor.objects.all()
        patient = Patient.objects.get(pk=1) #request.session.get["patientID"]
        return render(request,"hospital/appointments.html",context={
            "doctors":doctors,
            "patient":patient 
        })
    def post(self,request):
        userDate = request.POST["selected_date"]
        doctor = request.POST["doctors"]
        doctorObj = Doctor.objects.get(pk=int(doctor))
        patient = request.POST["patient"]
        patientObj = Patient.objects.get(pk=int(patient))
        inst = Appoinment(date = userDate)
        inst.save()
        inst.doctor.add(doctorObj)
        inst.patient.add(patientObj)
        return HttpResponseRedirect(reverse("patientDash"))


#############################
#                           #
#    End of Patient Views   #
#                           #
#############################






def contactUs(request):
    return render(request,'hospital/contactus.html')


def diseasePrediction(request):
    return HttpResponse("Hello World")