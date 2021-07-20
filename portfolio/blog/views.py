from django.shortcuts import render
from .models import ContactMeTable
from .forms import user_contact_form

def blog(request):
    return render(request,'blog/blog.html')

def bio(request):
    return render(request,'blog/bio.html')

def education(request):
    return render(request,'blog/education.html')

def contact(request):
    if request.method == "POST":
        form = user_contact_form(request.POST)
        if form.is_valid():
            data = ContactMeTable(name=form.cleaned_data['name'], email=form.cleaned_data['email'], info=form.cleaned_data['additionaldetails'])
            data.save()
        return render(request,'blog/thankyou_page.html')
    else:
        form = user_contact_form()
        return render(request,'blog/contact.html',{'form':form})

def thankyou(request):
    return render(request,'blog/thankyou_page.html')