from django.shortcuts import render, redirect
from django.contrib import messages
# this uses premade forms from django
# from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def login_page(request):
    """ render the login page to the user """
    if request.method == "GET":
        return render(request, "login.html")
    elif request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        # print(username, password)
    return render(request, "login.html")

def register_page(request):
    """ render the registration page """
    if request.method == "GET":
        return render(request, "register.html")
    elif request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        messages.success(request, f"Account for {username} created!")
        return redirect("login_page")
    return render(request, "register.html")