from django.shortcuts import render
from django.http import HttpResponse
from .models import Currency
import requests
import json
# Create your views here.
def index(request):
    return render(request, "index.html")

def home(request): 
    if request.method == "GET":
        base = request.GET['base'] 
        url = "https://api.exchangeratesapi.io/latest?base=" + base
        response = requests.get(url) 
        data = response.text 
        parsed = json.loads(data) 
        rates = parsed["rates"]
        data = {"x2":base,"ratez":rates}
        if not Currency.objects.filter(currency_code=base).exists():
            got = Currency()
            got.currency_code = request.GET.get('base')
            got.counts = 0
            got.save()
    return render(request, "home.html",data)

def result(request):
    if request.method == "GET":
        base = request.GET['base'] 
        query_set = Currency.objects.filter(currency_code=base)
        for i in query_set:
            i.counts += 1
            i.save()
    return render(request, "result.html", {"str1": query_set})

def top3(request):
    qs = Currency.objects.all().order_by('-counts')[0:3]
    return render(request, 'top3.html', {"str2":qs})





    