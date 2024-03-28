from django.shortcuts import render, redirect
from django.contrib import messages
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from app.forms import LoginForm

# Create your views here.


def home_page(request: HttpRequest) -> HttpResponse:
    context = {}
    return render(request, "home.html", context)


def about_page(request: HttpRequest) -> HttpResponse:
    context = {}
    return render(request, "about.html", context)


def gallery_page(request: HttpRequest) -> HttpResponse:
    context = {}
    return render(request, "gallery.html", context)


def booking_page(request: HttpRequest) -> HttpResponse:
    context = {}
    return render(request, "booking.html", context)


def owner_login(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                # Valid Login Information
                return redirect("ownerDashboard")
            else:
                # Invalid Login Information
                messages.info(request, "Invalid username or password")
    else:
        form = LoginForm()

    return render(request, "login.html", {"form": form})


@login_required(login_url="ownerLogin")
def owner_dash(request: HttpRequest) -> HttpResponse:
    context = {}
    return render(request, "owner_dash.html", context)
