# forms.py

from django import forms

class MessageForm(forms.Form):
    message = forms.CharField(widget=forms.Textarea, label='Message')
    address = forms.CharField(max_length=255, label='Address')
