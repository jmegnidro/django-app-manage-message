from django import forms
from django.forms import ModelForm

from .models import EmailCampagne, Messages, MessagesDiffusion, ClientBoxs


class ClientRegisterSms(forms.ModelForm):
    class Meta:
        model = ClientBoxs
        fields = ['last_name', 'first_name', 'email', 'telephone', 'address']
        widgets = {
            "last_name": forms.TextInput(attrs={'class': 'form-control custom-border'}),
            "first_name": forms.TextInput(attrs={'class': 'form-control custom-border'}),
            "email": forms.EmailInput(attrs={'class': 'form-control custom-border'}),
            "telephone": forms.TextInput(attrs={'class': 'form-control custom-border'}),
            "address": forms.Textarea(attrs={'class': 'form-control custom-border'})
        }
        labels = {
            "last_name": "Numero destinataire",
            "first_name": "Numero d'Envoi",
            "email": "email",
            "telephone": "telephone",
            "address": "address"
        }
        placeholders = {
            "last_name": "Nom",
            "first_name": "prenom(s)",
            "email": "email",
            "telephone": "telephone",
            "address": "Address du client"
        }


class MessageBoxForm(forms.ModelForm):
    class Meta:
        model = Messages
        fields = ['recipient', 'sender', 'corps']
        widgets = {
            "recipient": forms.Select(attrs={'class': 'form-control custom-border'}),
            "sender": forms.Select(attrs={'class': 'form-control custom-border'}),
            "corps": forms.Textarea(attrs={'class': 'form-control custom-border'})
        }
        labels = {
            "recipient": "Numero destinataire",
            "sender": "Numero d'Envoi",
            "corps": "Message"
        }
        placeholders = {
            "recipient": "Numero de destination",
            "sender": "numero d'envoi de message",
            "corps": "Rédiger votre message ici..."
        }

    def __init__(self, *args, **kwargs):
        super(MessageBoxForm, self).__init__(*args, **kwargs)
        self.fields['recipient'].widget.attrs.update({'class': 'form-control col-8'})
        self.fields['sender'].widget.attrs.update({'class': 'form-control col-8'})
        self.fields['corps'].widget.attrs.update({'class': 'form-control col-8'})


# diffusion multiple
class MessageBoxFormMutliple(forms.ModelForm):
    class Meta:
        model = MessagesDiffusion
        exclude = ['id', ]
        fields = ['recipient', 'sender', 'corps']
        widgets = {
            "recipient": forms.SelectMultiple(attrs={'class': 'form-control custom-border'}),
            "sender": forms.Select(attrs={'class': 'form-control custom-border'}),
            "corps": forms.Textarea(attrs={'class': 'form-control custom-border'})
        }
        labels = {
            "recipient": "Numero destinataire",
            "sender": "Numero d'Envoi",
            "corps": "Message"
        }
        placeholders = {
            "recipient": "Numero de destination",
            "sender": "numero d'envoi de message",
            "corps": "Rédiger votre message ici..."
        }


class EmaailCampagneForm(ModelForm):
    """class Meta:
        model = EmailCampagne
        exclude = ['id', ]
        fields = ['recipient', 'sender', 'corps']
        widgets = {
            "recipient": forms.SelectMultiple(attrs={'class': 'form-control custom-border'}),
            "sender": forms.Select(attrs={'class': 'form-control custom-border'}),
            "corps": forms.Textarea(attrs={'class': 'form-control custom-border'})
        }
        recipient = forms.ModelMultipleChoiceField(
            queryset=MessagesDiffusion.objects.all(),
            # Remplacez le queryset avec la requête pour récupérer les objets de modèle Telephone
            widget=forms.SelectMultiple(attrs={'class': 'form-control custom-border'}),
            to_field_name='email'  # Spécifiez le champ que vous voulez utiliser comme valeur dans le widget
        )
        labels = {
            "recipient": "Numero destinataire",
            "sender": "Numero d'Envoi",
            "corps": "Message"
        }
        placeholders = {
            "recipient": "Numero de destination",
            "sender": "numero d'envoi de message",
            "corps": "Rédiger votre message ici..."
        }
"""