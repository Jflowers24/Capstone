from django.shortcuts import render
from django.http.request import HttpRequest
from django.http.response import HttpResponse

# Create your views here.


def home_page(request: HttpRequest) -> HttpResponse:
    context = {}
    return render(request, "home.html", context)
