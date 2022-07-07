from django.shortcuts import render

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
                  context)