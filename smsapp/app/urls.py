from django.urls import path

from .views import contact_view, monosms, multidifusionsms, whtasappdiffusionMuliple, whtasapp, dashbordsms,\
    whatsapp


app_name = 'emails'
urlpatterns = [
    path('create', contact_view, name='create'),
    path('sms', monosms, name='sms'),
    path('diffusion/', multidifusionsms, name='multififusion'),
    path('whatsapp/', whtasapp, name='whatsapp'),
    path('diffusion-multiple/', whtasappdiffusionMuliple, name='whatdiffusion'),
    path('dashbord/', dashbordsms, name='dashbord')

]
