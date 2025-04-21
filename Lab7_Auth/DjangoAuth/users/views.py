from django.shortcuts import render,redirect
from django.contrib.auth import logout
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView

# Create your views here.


def home(request):
    return render(request, "users/home.html")



def logout_req(request):
    logout(request)
    return redirect("login")



class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = "registration/signup.html"
