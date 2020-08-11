from django.shortcuts import render
from django.http import HttpResponse
from .Task1function import loop
import json
# Create your views here.
def index(request,a,c):
    return HttpResponse(loop(a,c))