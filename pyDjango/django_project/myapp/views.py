from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Hello(request):
    text = '''<h1> Welcom to my home!<h1>'''
    return HttpResponse(request)