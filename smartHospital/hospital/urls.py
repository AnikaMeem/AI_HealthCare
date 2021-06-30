from django.urls import path
from . import views

urlpatterns = [
    path("",views.home_page,name="homepage"),
    path("aboutus/",views.aboutus,name="aboutus"),
    path("adminlogin/",views.adminlogin,name="adminlogin"),
    path("patientlogin/",views.patientlogin,name="patientlogin"),
    path("doctorlogin/",views.doctorlogin,name="doctorlogin"),
    path('contactus/',views.contactUs,name="contactus")
]