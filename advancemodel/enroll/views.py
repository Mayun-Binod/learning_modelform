from django.shortcuts import render
from enroll.forms import StudentRegistration
from .models import User
# Create your views here.
def showformdata(request):
    if request.method == "POST":
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            # Process the valid form data
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            print(nm)
            print(em)
            print(pw)
            store=User(name=nm,email=em,password=pw)
            store.save()
    else:
        # Handle GET request by displaying a blank form
        fm = StudentRegistration()

    return render(request, 'enroll/userregistration.html', {"form": fm})