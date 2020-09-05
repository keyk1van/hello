from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def homePageInfo(request):
    return HttpResponse("salam bar hame")