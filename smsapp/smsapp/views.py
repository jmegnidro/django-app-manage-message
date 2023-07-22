from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from account.models import CustomUser
from app.models import ClientBoxs, Messages, MessagesDiffusion, MessagesWhatsapp, EmailCampagne, Entreprise


def home(request):
    total_client_counts = ClientBoxs.objects.all().count()
    sms_count = Messages.objects.all().count()
    email_counts = EmailCampagne.objects.all().count()
    whatsapp_counts = MessagesWhatsapp.objects.all().count()
    sms_count_diffusion = MessagesDiffusion.objects.all().count()
    mail_whatsapp = MessagesWhatsapp.objects.all().count()
    customer_count = CustomUser.objects.all().count()
    sms_sender_counts = Entreprise.objects.all().count()

    context = {
        "total_client_counts": total_client_counts,
        "sms_count":sms_count,
        "email_counts": email_counts,
        "whatsapp_counts":whatsapp_counts,
        "sms_count_diffusion":sms_count_diffusion,
        "mail_whatsapp": mail_whatsapp,
        "customer_count":customer_count,
        "sms_sender_counts":sms_sender_counts
    }
    return render(request, 'home/index.html', context)


def us(request):
    return render(request, 'dash/usdash.html')
