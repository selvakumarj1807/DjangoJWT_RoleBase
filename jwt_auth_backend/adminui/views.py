from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def custom_login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user is not None and user.is_staff:
            login(request, user)
            return redirect("/auth/")  # Redirect to protected admin page
        else:
            messages.error(request, "Invalid credentials or unauthorized access.")
            return redirect("/")

    return render(request, "adminUI/login.html")

