from django.http import HttpResponse
from django.urls import include, path
from django.contrib import admin

def home(request):
    return HttpResponse("Welcome to the home page.")
