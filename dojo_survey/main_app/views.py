from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return render(request, 'index.html')

def result(request):
    print(request.POST)
    name_from_form = request.POST['your_name']
    location_from_form = request.POST['dojo_location']
    language_from_form = request.POST['favorite_language']
    comments_from_form = request.POST['comments']
    print(name_from_form)
    print(location_from_form)
    print(language_from_form)
    print(comments_from_form)
    context = {
        "name_from_template" : name_from_form,
        "location_from_template" : location_from_form,
        "language_from_template" : language_from_form,
        "comments_from_template" : comments_from_form
    }
    return render(request, 'result.html', context)