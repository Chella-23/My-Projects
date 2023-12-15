from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def display_view(request):
    s='<h1>Welcome to our Django first Application</h1>'
    return HttpResponse(s)
