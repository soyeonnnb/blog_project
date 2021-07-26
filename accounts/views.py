from django.shortcuts import render, redirect
from django.contrib import auth


def login(request):
    if request.method == "POST":
        userid = request.POST["username"]
        pwd = request.POST["password"]
        user = auth.authenticate(request, username=userid, password=pwd)
        if user is not None:
            auth.login(request, user)
            return redirect("home")
        else:
            return render(request, "bad_login.html")

    else:
        return render(request, "login.html")


def logout(request):
    auth.logout(request)
    return redirect("home")
