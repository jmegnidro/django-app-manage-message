from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render
from .forms import EmaailCampagneForm, MessageBoxForm, MessageBoxFormMutliple
from .models import Messages, MessagesDiffusion, MessagesWhatsapp


def monosms(request):
    if request.method == 'POST':
        form = MessageBoxForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = MessageBoxForm()
    return render(request, 'sms/monosms.html', {"form": form})


# mutlidifusion vues
def multidifusionsms(request):
    if request.method == 'POST':
        forms = MessageBoxFormMutliple(request.POST)
        if forms.is_valid():
            forms.save()
    else:
        forms = MessageBoxFormMutliple()
    return render(request, 'sms/multidiffusion.html', {"forms": forms})


def contact_view(request):
    if request.method == 'POST':
        form = EmaailCampagneForm(request.POST)
        if form.is_valid():
            form.save()
            email_subject = f'New contact {form.cleaned_data["email"]}: {form.cleaned_data["subject"]}'
            email_message = form.cleaned_data['message']
            attachement_piece = form.cleaned_data['attachement_piece']
            send_mail(email_subject, email_message, attachement_piece, settings.CONTACT_EMAIL, settings.ADMIN_EMAIL)
            return render(request, 'home/success.html')
    form = EmaailCampagneForm()
    context = {'form': form}
    return render(request, 'home/contact.html', context)


def dashbordsms(request):
    forms = Messages.objects.all()
    querysets = MessagesDiffusion.objects.all()

    contexte = {
        'forms': forms,
        'querysets': querysets
    }
    return render(request, 'dash/dashsms.html', contexte)


def whatsapp(request):
    querysets = MessagesWhatsapp.objects.all()
    contexte = {
        'querysets': querysets
    }
    return render(request, 'dash/whtasapp.html', contexte)


def createsmsdiffusuion(request):
    # la requete pour prendre en compte le formulaire
    return render(request, 'sms/multidiffusion.html')


def whtasapp(request):
    # la requete pour prendre en compte le formulaire
    return render(request, 'whtasapp/monodiffusion.html')


def whtasappdiffusionMuliple(request):
    # la requete pour prendre en compte le formulaire
    return render(request, 'whtasapp/mutlitidiffusion.html')
