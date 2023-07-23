from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from .forms import EmaailCampagneForm, MessageBoxForm, MessageBoxFormMutliple, ClientRegisterSms
from .models import Messages, MessagesDiffusion, MessagesWhatsapp, ClientBoxs


def enregistrer(request):
    if request.method == 'POST':
        client = ClientRegisterSms(request.POST)
        if client.is_valid():
            client.save()
        return render(request, 'client/voirclient.html')
    else:
        client = ClientRegisterSms()
    return render(request, 'client/client.html', {"client": client})


def voir(request):
    doms = ClientBoxs.objects.all()
    return render(request, 'client/voirclient.html', {"doms": doms})


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
        diffusions = MessageBoxFormMutliple(request.POST)
        if diffusions.is_valid():
            diffusions.save()
        return redirect('us', groupe_id=diffusions.instance.id)
    else:
        diffusions = MessageBoxFormMutliple()
    return render(request, 'sms/multidiffusion.html', {"diffusions": diffusions})


def contact_view(request):
    if request.method == 'POST':
        form = EmaailCampagneForm(request.POST)
        if form.is_valid():
            form.save()
            email_subject = f'New contact {form.cleaned_data["email"]}: {form.cleaned_data["subject"]}'
            email_message = form.cleaned_data['message']
            attachement_piece = form.cleaned_data['attachement_piece']
            send_mail(email_subject, email_message, attachement_piece, settings.CONTACT_EMAIL, settings.ADMIN_EMAIL)
            return redirect('us')
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


def whtasapp(request):
    # la requete pour prendre en compte le formulaire
    return render(request, 'whtasapp/monodiffusion.html')


def whtasappdiffusionMuliple(request):
    # la requete pour prendre en compte le formulaire
    return render(request, 'whtasapp/mutlitidiffusion.html')
