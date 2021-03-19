from django.shortcuts import render, redirect
from time import gmtime, strftime

def index(request):
    context = {
        "time": strftime("%Y-%m-%d %H:%M %p", gmtime())
    }
    return render(request, 'index.html')

def time(request):
    return redirect('/', 'index.html')

# Create your views here.
