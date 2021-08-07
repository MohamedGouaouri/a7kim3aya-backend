from django import forms
from django.forms import fields

from .models import Product


class ProdutForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'title', 'price', 'description'
        ]
