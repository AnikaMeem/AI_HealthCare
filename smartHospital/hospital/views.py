from django.shortcuts import render

# Create your views here.

def home_page(request):
    return render(request,'hospital/index.html')

def aboutus(request):
    return render(request,'hospital/aboutus.html')
