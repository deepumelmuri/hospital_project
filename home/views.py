from django.shortcuts import render
from django.http import HttpResponse
from . models import Departments,Doctors
from . forms import BookingForm



# Create your views here.
def base(request):
    return render(request,'base.html')
def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')
def doctors(request):
    dict_docs={
        'docs':Doctors.objects.all()
    }
    return render(request,'doctors.html',dict_docs)
def index(request):
    return render(request,'index.html')
def department(request):
    dict_dept={
        'dept':Departments.objects.all()
    }
    return render(request,'departments.html',dict_dept)
def booking(request):
    if request.method=="POST":
        form=BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'confirmation.html')
    form=BookingForm()
    dict_form={
        'form':form
    }
    return render(request,'booking.html',dict_form)

