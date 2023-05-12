from django import forms
from  django.forms import ModelForm
from .models import AnimalOwner


class AnimalOwner(ModelForm):
    class Meta:
        model = AnimalOwner
        fields = "__all__"