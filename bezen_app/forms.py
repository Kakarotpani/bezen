from django import forms
from .models import *


class RecipeUpdateForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = ("f_name", "f_description",
                  "ingredients", "f_procedure", "f_photo")


class RecipeAddForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = ("f_name", "f_description",
                  "ingredients", "f_procedure", "f_photo")
