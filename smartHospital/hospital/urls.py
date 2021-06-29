from django.urls import path
from . import views

urlpatterns = [
    path("",views.home_page,name="homepage"),
    path("aboutus/",views.aboutus,name="aboutus")
]