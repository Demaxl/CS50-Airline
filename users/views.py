from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def index(request):
    # Each request passed to a url has a user object that represents the current user
    # Checks to see if the user is authenticated
    if not request.user.is_authenticated:
        # redirect them to the login view
        return HttpResponseRedirect(reverse("login"))

    return render(request, "user.html")

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        # Checks to see if login creditianls are valid
        user = authenticate(request, username=username, password=password)

        # If they are valid a user object is returned, else none
        if user is not None:
            print(user)
            # Logs the user in
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "login.html", {
                "message":"Invalid credentials"
            })

    return render(request, "login.html", {})

def logout_view(request):
    # Logs out
    logout(request)
    return render(request, "login.html", {
        "message": "Successfully logged out"
    })