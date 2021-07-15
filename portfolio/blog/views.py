from django.shortcuts import render
from .models import STUDENTS

def blog(request):
    data = STUDENTS.objects.all()
    return render(request,'blog/blog.html',{"data":data})

def bio(request):
    return render(request,'blog/bio.html')

def education(request):
    return render(request,'blog/education.html')

def activities(request):
    return render(request,'blog/activities.html')

