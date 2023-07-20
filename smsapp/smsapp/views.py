from django.contrib.auth.decorators import login_required
from django.shortcuts import render


def home(request):
    return render(request, 'home/index.html')


def us(request):
    return render(request, 'dash/usdash.html')
