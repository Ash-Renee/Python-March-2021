from django.shortcuts import render, redirect
from .models import User

# Create your views here.
def index(request):
    context = {
        "all_user": User.objects.all()
    }
    return render(request, 'index.html', context)


def add_user(request):
    new_user = User.objects.create(
        name = request.POST["name"],
        email = request.POST["email"],
        age = request.POST["age"]
    )
    print(f"New User ID: {new_user.id}")
    return redirect ('/', 'index.html')
