from django.shortcuts import render
from django.http import HttpResponse
from .models import Rooms
from .forms import Bookingform




def home(request):
    return render(request,'home.html')
def about(request):
    return render(request,'about.html')
def rooms(request):
    dict_ro={
        'ro':Rooms.objects.all()
    }
    return render(request,'rooms.html',dict_ro)
def contactus(request):
    return render(request,'contactus.html')
def booking(request):
    if request.method=='POST':
        form=Bookingform(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'confirmation.html')
    form=Bookingform()
    dict_form={
        'form':form
    }
    return render(request, 'booking.html',dict_form)