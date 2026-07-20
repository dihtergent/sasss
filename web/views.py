from django.shortcuts import render,HttpResponse
from django.http import HttpResponse
# Create your views here.
def index (request) :
    import datetime
    context = {
        "title" : "my home page",
    }

    context["date"] = datetime.date.today()
    return render(request,'index.html')
def about (request) :
    return HttpResponse("about")
def contact (request) :
    return HttpResponse("contact")