from django.shortcuts import render

# Create your views here.
def login_page(request):
    """ render the login page to the user """
    return render(request, "login.html")

def register_page(request):
    """ render the registration page """
    return render(request, "register.html")