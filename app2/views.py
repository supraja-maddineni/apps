from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def app2_first(request):
    return HttpResponse('<h3>This is the first function in app2</h3>')
def app2_second(request):
    return HttpResponse('<h3>This is the second function in app2</h3>')