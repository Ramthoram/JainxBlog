from django.shortcuts import render
from django.http import HttpResponse
from .models import blog


# Create your views here.
def homepage(request):
    return HttpResponse("This is My FirstApp")

def hom(request):
    return render(request,"base.html",{"name" : "Sairam"})

def about(request):
    return render(request,"about.html")

def blogg(request):
    post= blog.objects.all()
    return render(request,"blog.html",{'post':post})