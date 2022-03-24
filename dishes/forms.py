from django import forms
from django.forms import ModelForm
from .models import *


class PersonForm(ModelForm):

    class Meta:
        model = Person
        fields = ['name', 'surname']


class SaladForm(ModelForm):

    class Meta:
        model = Salad
        fields = '__all__'


class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()
