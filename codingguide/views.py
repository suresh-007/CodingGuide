from django.shortcuts import render

from django.http import HttpResponse

def home(request):
    return HttpResponse('<h1>Welcome</h1><a href="infy_questions/">questions</a>')