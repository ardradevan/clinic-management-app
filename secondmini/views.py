from django.shortcuts import render,redirect
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from .models import Departments,Doctors
from .forms import BookingForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request,'index.html')

def register_view(request):
    form=UserCreationForm()
    if request.method == 'POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            print('sucessfully registered')
            return redirect(reverse('register'))
    return render(request,'accounts/register.html',{'form':form})

def homeview(request):
    return render(request,'home.html')

@login_required
def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')


@login_required
def department(request):
    dict_dept={
        'dept':Departments.objects.all()
    }
    return render(request,'dep.html', dict_dept)

@login_required()
def doctors(request):
    dict_docs={
        'doctors':Doctors.objects.all()
    }
    return render(request,'doctors.html',dict_docs)

@login_required
def booking(request):
    if request.method == "POST":
        print(request.POST)
        form =BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'confirm.html')
        else:
            return render(request,'booking.html', {'form':form})
    form=BookingForm()
    return render(request,'booking.html', {'form': form})
