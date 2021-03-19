from django.shortcuts import render, redirect
import random

# Create your views here.
def index(request):
    if "answer" not in request.session:
        request.session["answer"] = random.randint(1,100)
    print (request.session["answer"])
    return render(request, 'index.html')

def replay(request):
    request.session["result"] = int(request.POST["guess"])
    return redirect('/')


def clear(request):
    del request.session["answer"]
    del request.session["result"]
    return redirect('/')