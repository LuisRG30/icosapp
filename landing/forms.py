from django import forms
from django.forms import ModelForm
from .models import Message

class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ('name', 'email', 'message')
        widgets = {
            'message': forms.Textarea()
        }