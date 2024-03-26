from django.shortcuts import render
from django.http.request import HttpRequest
from django.http.response import HttpResponse

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
    context = {}
    return render(request, "owner_login.html", context)


def owner_dash(request: HttpRequest) -> HttpResponse:
    context = {}
    return render(request, "owner_dash.html", context)
