from django import forms
from .models import Archivo


class ArchivoForm(forms.Form):
    archivo = forms.FileField()

