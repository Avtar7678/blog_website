from django.shortcuts import render
from index import views

# Create your views here.
def home (request):
    return render(request,"home.html")
def about(request):
    return render(request,"about.html")
def project(request):
    return render(request,"project.html")
def contact(request):
    return render(request,"contact.html")
def r_1(request):
    return render(request,"r_1.html")
