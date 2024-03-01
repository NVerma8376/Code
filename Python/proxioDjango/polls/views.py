from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def polls(request):
    template = loader.get_template("polls.html")
    return HttpResponse(template.render())
# Create your views here.
