from django.contrib import admin
from twilio.twiml.voice_response import Client

from .models import ClientBoxs, Entreprise, Messages, MessagesDiffusion, MessagesWhatsapp, EmailCampagne


class MessageAdmin(admin.ModelAdmin):
    list_display = ['id', 'sender', 'corps']


admin.site.register(Messages, MessageAdmin)


class ClientAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'telephone', 'address', 'created_at']
    list_filter = ['first_name', 'last_name', 'email', 'telephone']


admin.site.register(ClientBoxs, ClientAdmin)
admin.site.register(Entreprise)


class MessageAdminDiffusionMultiple(admin.ModelAdmin):
    list_display = ['get_first_recipient_name', 'id', 'sender', 'corps']

    def get_first_recipient_name(self, obj):
        first_recipient = obj.recipient.first()
        if first_recipient:
            return first_recipient.first_name
        return ""

    get_first_recipient_name.short_description = 'Recipient'


admin.site.register(MessagesDiffusion, MessageAdminDiffusionMultiple)


class MessageAdminDiffusionMultipleWhatsapp(admin.ModelAdmin):
    list_display = ['get_first_recipient_name', 'id', 'sender', 'corps']

    def get_first_recipient_name(self, obj):
        return obj.recipient.first().first_name

    get_first_recipient_name.short_description = 'Recipient'


admin.site.register(MessagesWhatsapp, MessageAdminDiffusionMultipleWhatsapp)


admin.site.register(EmailCampagne)