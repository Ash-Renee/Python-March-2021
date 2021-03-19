from django.shortcuts import render, redirect

# Create your views here.

def index(request):
    if 'click_count' in request.session:
        request.session ['click_count'] += 1
    else:
        request.session ['click_count'] = 0
    return render(request, 'index.html')

def clear(request):
    try:
        del request.session['click_count']
    except:
        print("No click count in session")
    return redirect('/')

def add2(request):
    if 'click_count' in request.session:
        request.session ['click_count'] += 2
    else:
        request.session ['click_count'] = 0
    return render(request, 'index.html')