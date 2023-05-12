import os
from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from .models import AnimalOwner

def home(request):
    return render(request,'home.html',{})


def Appoint(request):
    return render(request,'Appoint.html',{})


def DoctorP(request):
    return render(request,'DoctorP.html',{})

def Contact(request):
    return render(request,'Contact.html',{})

def FindDoc(request):
    return render(request,'FindDoc.html',{})

def MedInfo(request):
    return render(request,'MedInfo.html',{})


def A(request):
    return render(request,'A.html',{})


def B(request):
    return render(request,'B.html',{})


def C(request):
    return render(request,'C.html',{})


def AnimalOwner_DB(request):
    all_petOwners =AnimalOwner.objects.all
    return render(request,'AnimalOwner_DB.html',{'all':all_petOwners})









def UserP(request):
    all_members = AnimalOwner.objects.all
    return render(request,'UserP.html',{'all':all_members})

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect


def signin_form(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.groups.filter(name='Hospital Staff').exists():
                login(request, user)
                return redirect('DoctorP')
            elif user.groups.filter(name='Pet Owners').exists():
                login(request, user)
                return redirect('UserP')
            else:
                # Invalid user group
                return render(request, 'home.html', {'message': 'Invalid user group'})
        else:
            # Invalid username or password
            return render(request, 'home.html', {'message': 'Invalid username or password'}) #Redirect to error page
    else:
        return render(request, 'signin_form.html')



def doctor_profile(request):
    # Fetch doctor information and credentials from the database
    doctor_info = ...
    doctor_credentials = ...

    # Fetch appointments for the doctor from the database
    appointments = ...

    # Fetch animals under the doctor's care and their medical history from the database
    animals = ...

    context = {
        'doctor_info': doctor_info,
        'doctor_credentials': doctor_credentials,
        'appointments': appointments,
        'animals': animals,
    }

    return render(request, 'doctor_profile.html', context)