from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from twilio.rest import Client


class Entreprise(models.Model):
    telephon = PhoneNumberField()
    email = models.EmailField()
    name = models.CharField(max_length=45)

    def __str__(self):
        return str(self.telephon)


class ClientBoxs(models.Model):
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(max_length=100)
    telephone = PhoneNumberField()
    address = models.CharField(max_length=200, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.telephone)

    class Meta:
        ordering = ['-created_at']


class Messages(models.Model):
    recipient = models.ForeignKey(ClientBoxs, on_delete=models.CASCADE)
    sender = models.ForeignKey(Entreprise, on_delete=models.CASCADE)
    corps = models.TextField(max_length=160)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.corps

    def save(self, *args, **kwargs):
        if len(self.corps) < 160:
            account_sid = 'ACef63632b0ba2a47909195de3b18c6d65'
            auth_token = 'd84211952960f5b6780aac91474cba2e'
            client = Client(account_sid, auth_token)

            message = client.messages.create(
                body=f"{self.corps}",
                from_=f'{self.sender.telephon}',
                to=f'+{self.recipient.telephone}'
            )
            print(message)
        else:
            return None

        super().save()


class MessagesDiffusion(models.Model):
    recipient = models.ManyToManyField(ClientBoxs)  # Correction : supprimer primary_key={}
    sender = models.ForeignKey(Entreprise, on_delete=models.CASCADE)
    corps = models.TextField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.corps

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.recipient.count() <= 100:
            account_sid = 'ACef63632b0ba2a47909195de3b18c6d65'
            auth_token = 'd84211952960f5b6780aac91474cba2e'
            client = Client(account_sid, auth_token)

            for recipient in self.recipient.all():
                try:
                    message = client.messages.create(
                        body=f"{self.corps}",
                        from_=f'{self.sender.telephon}',
                        to=f'+{recipient.telephone}'
                    )
                    print(message)
                except Exception as e:
                    print(f"Erreur lors de l'envoi du message au destinataire {recipient}: {str(e)}")


class MessagesWhatsapp(models.Model):
    recipient = models.ManyToManyField(ClientBoxs)
    sender = models.ForeignKey(Entreprise, on_delete=models.CASCADE)
    corps = models.TextField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.corps

    def save(self, *args, **kwargs):
        if self.recipient.count() <= 1000:
            account_sid = 'ACef63632b0ba2a47909195de3b18c6d65'
            auth_token = 'd84211952960f5b6780aac91474cba2e'
            client = Client(account_sid, auth_token)

            message = client.messages.create(
                body=f"{self.corps}",
                from_=f'{self.sender.telephon}',
                to=f'+{self.recipient.telephone}'
            )
            print(message)
        else:
            return None


class EmailCampagne(models.Model):
    email = models.EmailField()
    subject = models.CharField(max_length=150, verbose_name='Objet')
    message = models.TextField(max_length=1000)
    attachement_piece = models.FileField(blank=True, null=True, verbose_name='piece jointe',
                                         upload_to='emailattachement')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject

    def get_recipient_mail(self):
        emails = self.email.all()
        recipient_emails = [email.email for email in emails]
        return ", ".join(recipient_emails)
