from django.urls import path

from .views import contact_view, monosms, multidifusionsms, whtasappdiffusionMuliple, whtasapp, dashbordsms, enregistrer, voir


app_name = 'emails'
urlpatterns = [
    path('create', contact_view, name='create'),
    path('enregistrer/client/', enregistrer, name='client'),
    path('voir/client/', voir, name='clients'),
    path('sms', monosms, name='sms'),
    path('diffusion/', multidifusionsms, name='multififusion'),
    path('whatsapp/', whtasapp, name='whatsapp'),
    path('diffusion-multiple/', whtasappdiffusionMuliple, name='whatdiffusion'),
    path('dashbord/', dashbordsms, name='dashbord')

]
