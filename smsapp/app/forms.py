from django import forms
from django.forms import ModelForm

from .models import EmailCampagne, ClientBoxs, Messages, MessagesDiffusion


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

    def __init__(self, *args, **kwargs):
        super(MessageBoxFormMutliple, self).__init__(*args, **kwargs)
        self.fields['recipient'].widget.attrs.update({'class': 'form-control col-8'})
        self.fields['sender'].widget.attrs.update({'class': 'form-control col-8'})
        self.fields['corps'].widget.attrs.update({'class': 'form-control col-8'})


class EmaailCampagneForm(ModelForm):
    class Meta:
        model = EmailCampagne
        fields = '__all__'
        widgets = {
            'email': forms.CheckboxSelectMultiple,
            'message': forms.Textarea(attrs={'rows': 4}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].queryset = ClientBoxs.objects.all()


class SmsFormSimpleForm(forms.ModelForm):
    pass
