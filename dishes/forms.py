from attr import fields
from django import forms
from django.forms import ModelForm
from numpy import product
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


class UploadBook(ModelForm):
    class Meta:
        model = Book
        fields = '__all__'


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
