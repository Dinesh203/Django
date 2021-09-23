from django.shortcuts import render, HttpResponseRedirect
from .forms import StudentRegistration
from .models import User
from django.contrib import messages



def Add_Show(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            # nm = fm.cleaned_data['name']
            # em = fm.cleaned_data['email']
            # pd = fm.cleaned_data['password']
            # reg = User(name=nm, email=em, password=pd)
            # reg.save()
            fm.save()
            fm = StudentRegistration()
    else:
        fm = StudentRegistration()
    stud = User.objects.all()
    return render(request, 'enroll/add_show.html', {'form' : fm, 'stu': stud})


def delete_data(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')

def update_date(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
            messages.success(request, "Update Successfully!")
            fm = StudentRegistration()

    else:
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(instance=pi)
    return render(request, 'enroll/update_student.html', {'form': fm})
