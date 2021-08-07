from django.urls import path
from . import views
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
    path("",views.home_page,name = "homepage"),
    path("aboutus/",views.aboutus,name = "aboutus"),
    path("patientlogin/",views.PatientLogin.as_view(),name = "patientlogin"),
    path("doctorlogin/",views.doctorlogin,name = "doctorlogin"),
    path("doctorSignin/",views.Signin.as_view(),name="doctorSignin"),
    path('contactus/',views.contactUs,name = "contactus"),
    path("doctorDash/",views.DoctorDash.as_view(),name = "doctorDash"),
    path("patientDash/",views.PatientDash.as_view(),name = "patientDash"),
    path("diseasePrediction/",views.diseasePrediction,name = "diseasePrediction"),
    path("appointment/",views.Appoinments.as_view(),name = "appointment")
]