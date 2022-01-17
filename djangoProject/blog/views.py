from curses.ascii import HT
from django.shortcuts import render ,HttpResponse
from blog.models import Contact
from datetime import datetime
from django.contrib import messages

# Create your views here.
def index(request):
    content={
        "name":"tayyab",
        "lastname":"ashraf"
    }
    return render(request,'index.html',content)
    # return HttpResponse("Hellow World")
def about(request):
    return render(request,'about.html')
    # return HttpResponse("This is about page")
def services(request):
    return render(request, 'services.html')
    # return HttpResponse("this is Services page")
def contect(request):
    if request.method=="POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        msg = request.POST.get('msg')
        contact = Contact(name=name,email = email,  phone=phone,msg=msg, date=datetime.today())
        contact.save()
        messages.success(request, 'Your Message has been Send Successfully.')

    return render(request,'contect.html')
    # return HttpResponse("this is the contect us page")
