from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *

""" class UserForm(forms.ModelForm):   
    confirm_password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ("username", "email", "password")
        widgets =  {'password': forms.PasswordInput()}

    def clean(self):
        cleaned_data = super(UserForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError("password and confirm_password does not match") """