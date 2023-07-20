from django.urls import path, include
from .views import register, connexion
from django.contrib.auth import views as auth_views


app_name = 'accounts'
urlpatterns = [
    path("login/", connexion, name='login'),
    path('register/',  register, name='register'),

]
