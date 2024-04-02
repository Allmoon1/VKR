from django.shortcuts import render, redirect
from django.contrib import auth
from .forms import UserRegistrationForm
from .forms import UserAuthorizationForm
from .models import User
from .models import Song
from django.core.paginator import Paginator

def index(request):
    if not request.user.is_authenticated:
        return render(request, 'main/index.html')

    search_query = request.GET.get("q")
    records = ""
    if search_query == None:
        records = "Not found"
    else:
        records = Song.objects.filter(song_title__contains = search_query)
    print(records)
    return render(request, 'main/index.html', {
        'records':records,
        })

def login(request):
    error = ""
    if request.method == "POST":
        form = UserAuthorizationForm(request.POST)
        if form.is_valid() and (User.objects.filter(username = form.cleaned_data.get("username"), password = form.cleaned_data.get("password")).exists()):
            error = "READY"
            return redirect(index)
        else:
            error = "ERROR: You dont reg"

    form = UserAuthorizationForm()
    data = {
        'form':form,
        'error':error
        }

    return render(request, 'main/login.html', data)


def register(request):
    error = ""
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid() and (form.cleaned_data.get("password") == form.cleaned_data.get("r_password")):
            form.save()
            error = ""
            return redirect(index)
        else:
            error = "Passwords invalid"

    form = UserRegistrationForm()
    data = {
        'form':form,
        'error':error
        }

    return render(request, 'main/register.html', data)


def logout(request):
    auth.logout(request)
    return redirect(index)


# Create your views here.
