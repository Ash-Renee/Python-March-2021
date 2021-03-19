from django.shortcuts import render, redirect, HttpResponse
from django.http import JsonResponse

def root_method(request):
    return redirect('/blogs')

def blogs(request):
    return render(request, 'index.html')

def new(request):
    return HttpResponse("placeholder to display a new form to create a new blog")

def create(request):
    return redirect('/blogs')

def show(request, num):
    return HttpResponse (f"placeholder to display blog number: {num}")

def edit(request, num):
    return HttpResponse(f"placeholder to edit blog {num}")

def destroy(request, num):
    return redirect('/blogs')

def bonus(request):
    return JsonResponse({"title": "my first blog", "content": "lorem......"})