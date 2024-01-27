from django.shortcuts import render, redirect
from .forms import UserForm
from .models import User

def index(request):
    return render(request, 'main/index.html')
def login(request):
    return render(request, 'main/login.html')




def register(request):

    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(login)

    form = UserForm()
    data = {
        'form':form
        }

    return render(request, 'main/register.html', data)



# Create your views here.
