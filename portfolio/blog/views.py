from django.shortcuts import render

def blog(request):
    return render(request,'blog/blog.html')

def bio(request):
    return render(request,'blog/bio.html')

def education(request):
    return render(request,'blog/education.html')

def activities(request):
    return render(request,'blog/activities.html')

