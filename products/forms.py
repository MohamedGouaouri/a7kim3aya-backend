from django import forms
from django.forms import fields

from .models import Product


class ProdutForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'title', 'price', 'description'
        ]


class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    f = forms.FileField()
