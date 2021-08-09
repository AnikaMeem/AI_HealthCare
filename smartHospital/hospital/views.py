from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect,HttpResponse
from django.views.generic import DetailView,View
from .models import Doctor,Patient,Appointment
from .forms import DoctorForm,PatientForm

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

    try:
        if request.session.get("doctorID"):
            return HttpResponseRedirect(reverse("doctorDash"))
        if request.method == "POST":
            email = request.POST["userEmail"]
            password = request.POST["userPassword"]
            doctor = Doctor.objects.get(email=email.lower())        
            if password == doctor.password:
                request.session["doctor"] = f"{doctor.first_name} {doctor.last_name}"
                request.session["doctorID"] = doctor.id
                return HttpResponseRedirect(reverse("doctorDash"))
        return render(request,'hospital/login.html',context={
            "title":"Doctor Login",
            "usertype":"Doctor Email",
            "image":"images/doctor.png"
            })
    except:
        return HttpResponse(f"Email: {request.POST['userEmail']} does not exist in database")


class DoctorDash(View):
    def get(self,request):
        if request.session.get("doctorID"):
            patients = []
            doctor = Doctor.objects.get(pk = request.session["doctorID"])
            appointments = Appointment.objects.filter(doctor=int(doctor.id))
            for item in appointments:
                name = Patient.objects.get(pk=int(item.patient)).first_name
                patients.append(name)
            for a,b in zip(appointments,patients):
                print(a.approved)
                print(b)
            hasAppointment = appointments.count()>0
            return render(request,"hospital/doctor_dash.html",context={
                "doctor" : doctor,
                "appointments": zip(appointments,patients),
                "hasAppointment": hasAppointment,
                "appointments2": zip(appointments,patients),
            })
        else:
            return HttpResponseRedirect(reverse("doctorlogin"))
    def post(self,request):
        if request.POST["logout"]:
            del request.session["doctor"]
            del request.session["doctorID"]
            return HttpResponseRedirect(reverse("homepage"))

def doctorSignin(request):
    form = DoctorForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse("success"))
    else:
        form = DoctorForm(request.POST or None)
        return render(request, "hospital/signin.html",context={
        "title": "Doctor Sign In",
        "form": form 
        })


#############################
#                           #
#    End of Doctor Views    #
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
        try:
            email = request.POST["userEmail"]
            password = request.POST["userPassword"]
            patient = Patient.objects.get(email=email.lower())        
            if password == patient.password:
                request.session["patient"] = f"{patient.first_name} {patient.last_name}"
                request.session["patientID"] = patient.id
                return HttpResponseRedirect(reverse('patientDash'))
        except:
            return HttpResponse(f"Email: {request.POST['userEmail']} doesn't exist in the database")



class PatientDash(View):
    def get(self,request):
        if request.session.get("patientID"):
            doctors = []
            patient = Patient.objects.get(pk = request.session.get("patientID"))
            appointment = Appointment.objects.filter(patient=patient.id)
            for doc in appointment:
                name = Doctor.objects.get(pk = int(doc.doctor)).first_name
                doctors.append(name)
            #print(appointment.patient.all())
            isEmpty = len(doctors)==0
            print(isEmpty)
            return render(request,"hospital/patient_dash.html",context={
                "patient" : patient,
                "appointments": zip(appointment,doctors),
                "appointmentCount": isEmpty
            })
        else:
            return HttpResponseRedirect(reverse("patientlogin"))
    def post(self,request):
            del request.session["patient"]
            del request.session["patientID"]
            return HttpResponseRedirect(reverse("homepage"))




class MakeAppointments(View):
    def get(self,request):
        if request.session["patientID"]:
            doctors = Doctor.objects.all()
            patient = Patient.objects.get(pk=int(request.session["patientID"])) 
            return render(request,"hospital/appointments.html",context={
                "doctors":doctors,
                "patient":patient 
            })
        else:
            return HttpResponseRedirect(reverse("patientlogin"))
    def post(self,request):
        userDate = request.POST["selected_date"]
        doctorID = request.POST["doctors"]
        patientID = request.POST["patient"]
        appointment = Appointment(doctor=doctorID,patient=patientID,date = userDate)
        appointment.save()
        return HttpResponseRedirect(reverse("patientDash"))

def patientSignin(request):
    form = PatientForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse("success"))
    else:
        form = PatientForm(request.POST or None)
        return render(request, "hospital/signin.html",context={
        "title": "Patient Sign In",
        "form": form 
        })


#############################
#                           #
#    End of Patient Views   #
#                           #
#############################





def contactUs(request):
    return render(request,'hospital/contactus.html')


def diseasePrediction(request):
    return HttpResponse("Hello World")

def success(request):
    return render(request, "hospital/success.html")

    