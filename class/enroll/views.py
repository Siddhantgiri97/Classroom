from django.shortcuts import render, HttpResponseRedirect
from .forms import StudentRegistration
from .models import User
# Create your views here.


def add_show(request):
    if request.method == 'POST':
        form = StudentRegistration(request.POST)
        if form.is_valid():
            nm = form.cleaned_data['name']
            em = form.cleaned_data['email']
            pd = form.cleaned_data['password']
            reg = User(name=nm, email=em, password=pd)
            reg.save()
            form = StudentRegistration()
    else:
        form = StudentRegistration()
    student = User.objects.all()
    context = {'form': form, 'student': student}
    return render(request, 'enroll/addandshow.html', context)


def update_data(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        form = StudentRegistration(request.POST, instance=pi)
        if form.is_valid():
            form.save()
    else:
        pi = User.objects.get(pk=id)
        form = StudentRegistration(instance=pi)
    return render(request, 'enroll/updatestudent.html', {'form': form})


def delete_data(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        pi.delete()
    return HttpResponseRedirect('/')
