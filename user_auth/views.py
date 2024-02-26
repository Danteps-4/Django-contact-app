from django.shortcuts import render, redirect
from .forms import SignInForm, SignUpForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.
def sign_in(request):
    if request.method == "GET":
        form = SignInForm()
        return render(request, "user_auth/sign_in.html", {"form": form})
    else:
        user = authenticate(request, username=request.POST["username"], password=request.POST["password"])
        if user:
            login(request, user)
            return redirect("core:home")
        else:
            form = SignInForm()
            return render(request, "user_auth/sign_in.html", {"form": form, "error": "Invalid credentials"})
        

def sign_up(request):
    if request.method == "GET":
        form = SignUpForm()
        return render(request, "user_auth/sign_up.html", {"form": form})
    else:
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("user_auth:sign_in")
        else:
            form = SignUpForm()
            return render(request, "user_auth/sign_up.html", {"form": form, "error": "Error"})

@login_required
def sign_out(request):
    logout(request)
    return redirect("user_auth:sign_in")