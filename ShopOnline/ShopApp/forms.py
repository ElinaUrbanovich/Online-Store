from django import forms
from django.core.exceptions import ValidationError
from .models import Order
from django.contrib.auth.models import User

class OrderForm(forms.Form):

    name = forms.CharField(max_length=255)
    surname = forms.CharField(max_length=255)
    email = forms.EmailField(max_length=255)
    address = forms.CharField(widget=forms.Textarea())
    city = forms.CharField(max_length=255)

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']