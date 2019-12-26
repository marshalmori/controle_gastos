from django.shortcuts import render
from django.http import HttpResponse
import datetime 

def home(request):
    now = datetime.datetime.now()
    return render(request,'contas/home.html')

