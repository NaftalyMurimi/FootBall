# forms.py

from django import forms

class MessageForm(forms.Form):
    message = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label='Message')
    address = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label='Number of Results')
