from django.shortcuts import render 
from django.http import HttpResponseRedirect
from .forms import StudentRegistration
from .models import User

# Create your views here.

# This function will add new item and show all items
def add_show(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            # nm=fm.cleaned_data['name']
            # em=fm.cleaned_data['email']
            # pw=fm.cleaned_data['password']
            # reg = User(name=nm,email=em,password=pw)
            fm.save()
            # reg.save()
            fm = StudentRegistration()
            
    else:
        fm = StudentRegistration()
    stud = User.objects.all()
    return render(request,'enroll/addAndShow.html',{'form':fm,'stu':stud})

# This Function will delete

def delete_data(request ,id):
    if request.method == 'POST':
        pi = User.objects.get(pk = id)
        pi.delete()
    return HttpResponseRedirect('/')


 # This function wiil for update 

def update_data(request,id):
    pi = User.objects.get(pk = id)

    if request.method == "POST":
        fm = StudentRegistration(request.POST,instance=pi)

        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect('/')
    else:
        fm = StudentRegistration(instance=pi)

    return render(request,'enroll/updateStudent.html',{"form":fm})
           