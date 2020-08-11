from django.shortcuts import render
from django.http import HttpResponse
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
    return render(request, "home.html",data)