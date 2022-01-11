from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from .models import BlogUsers
# this uses premade forms from django
# from django.contrib.auth.forms import UserCreationForm

def register_page(request):
    """ render the registration page """
    if request.method == "GET":
        return render(request, "register.html")
    elif request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        print(username, email, password)
        instance = User.objects.create_user(username=username, email=email, password=password)
        blog_user = BlogUsers(user=instance)
        blog_user.save()
        messages.success(request, f"Account for {username} created!")
        return redirect("login")
    return render(request, "register.html")