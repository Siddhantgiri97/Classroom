from django.shortcuts import render, HttpResponseRedirect
from .forms import StudentRegistration
from .models import User
from django.views.generic.base import TemplateView, RedirectView
from django.views import View
# Create your views here.


class UserAddShowView(TemplateView):
    template_name = 'enroll/addandshow.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        form = StudentRegistration()
        student = User.objects.all()
        context = {'form': form, 'student': student}
        return context

    def post(self, request):
        form = StudentRegistration(request.POST)
        if form.is_valid():
            nm = form.cleaned_data['name']
            em = form.cleaned_data['email']
            pd = form.cleaned_data['password']
            reg = User(name=nm, email=em, password=pd)
            reg.save()
        return HttpResponseRedirect('/')


class UserUpdateView(View):
    def get(self, request, id):
        pi = User.objects.get(pk=id)
        form = StudentRegistration(instance=pi)
        return render(request, 'enroll/updatestudent.html', {'form': form})

    def post(self, request, id):
        pi = User.objects.get(pk=id)
        form = StudentRegistration(request.POST, instance=pi)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/')


class UserDeleteView(RedirectView):
    url = '/'

    def get_redirect_url(self, *args, **kwargs):
        del_id = kwargs['id']
        User.objects.get(pk=del_id).delete()
        return super().get_redirect_url()
