from curses.ascii import HT
from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    context = {
        'variable':' Your Application has been sent Now '
    }
    return render(request,'index.html',context) 
    # return HttpResponse("This is the home page")

def about(request):
    return HttpResponse("This is the About Page in Django")
    
def contect(request):
    return HttpResponse("Wow, this is amazing and i'm working with django...Really amazing")
