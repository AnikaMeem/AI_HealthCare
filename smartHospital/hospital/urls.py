from django.urls import path
from . import views
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
    path("",views.home_page,name="homepage"),
    path("aboutus/",views.aboutus,name="aboutus"),
    path("patientlogin/",views.patientlogin,name="patientlogin"),
    path("doctorlogin/",views.doctorlogin,name="doctorlogin"),
    path('contactus/',views.contactUs,name="contactus"),
    path("doctorDash/",views.DoctorDash.as_view(),name="doctorDash"),
    path("diseasePrediction/",views.diseasePrediction,name="diseasePrediction"),
]