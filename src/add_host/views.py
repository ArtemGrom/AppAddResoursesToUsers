from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login
from django.views.generic.edit import FormView
from django.views.generic import ListView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from add_host.models import Host


class HostListView(LoginRequiredMixin, ListView):
    queryset = Host.objects.all()
    context_object_name = 'hosts'
    template_name = 'add_host/host/list_host.html'

    def get_queryset(self):
        return super().get_queryset().filter(owner=self.request.user)


def index(request):
    return render(request, 'add_host/index.html')


class RegisterFormView(FormView):
    form_class = UserCreationForm

    success_url = "/add_host/login_user/"
    template_name = "registration/login.html"

    def form_valid(self, form):
        form.save()
        return super(RegisterFormView, self).form_valid(form)


class LoginFormView(FormView):
    form_class = AuthenticationForm

    success_url = "/add_host/"
    template_name = "registration/login.html"

    def form_valid(self, form):
        self.user = form.get_user()
        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)









"""from django.shortcuts import render

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    return render(request, 'add_host/index.html')


def sign_up(request):
    context = {}
    form = UserCreationForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            user = form.save()
            login(request, user)
            return render(request,
                          'add_host/index.html')
    context['form'] = form
    return render(request,
                  'registration/login.html',
                  context)"""
