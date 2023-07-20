from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import get_user_model, authenticate
from django.views.generic import DetailView
from django.contrib.auth import login as log_user
from django.contrib.auth import logout as logout_user

CustomUser = get_user_model()


def connexion(request):
    if request.method == "POST":

        email = request.POST.get("email")
        password = request.POST.get("password")
        user = authenticate(email=email, password=password)
        if user is not None:
            log_user(request, user)
            return redirect("us")
        else:
            return render(request, "accounts/login.html", {
                "error": "Invalid username or password"
            })
    else:
        return render(request, "accounts/login.html")


def register(request):
    if request.method == 'POST':
        last_name = request.POST.get('last_name')
        first_name = request.POST.get('first_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Créer un nouvel utilisateur CustomUser
        user = CustomUser.objects.create_user(
            last_name=last_name,
            first_name=first_name,
            username=username,
            email=email,
            password=password
        )
        user.save()
        return redirect("us")

    return render(request, 'accounts/registration.html')


class DetailProfileView(DetailView):
    template_name = 'base.html'
    context_object_name = 'photo'
