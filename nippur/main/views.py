from django.shortcuts import render, redirect
from .forms import UserForm
from .models import User

def index(request):
    return render(request, 'main/index.html')
def login(request):
    return render(request, 'main/login.html')




def register(request):
    error = ""
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid() and (form.cleaned_data.get("password") == form.cleaned_data.get("r_password")):
            form.save()
            error = ""
            return redirect(index)
        else:
            error = "Passwords invalid"

    form = UserForm()
    data = {
        'form':form,
        'error':error
        }

    return render(request, 'main/register.html', data)



# Create your views here.
