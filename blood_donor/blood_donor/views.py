from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")

def register(request):
    if request.method == "POST":
        # TODO: Process form data
        pass
    return render(request, "register.html")

def search(request):
    # TODO: Implement search functionality
    return render(request, "search.html")

def profile(request):
    # TODO: Display user's profile information
    return render(request, "profile.html")