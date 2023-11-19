# forms.py
from django import forms


class Form(forms.Form):
    CATEGORY_CHOICES = [
        ('1', 'banque'),
        ('2', 'caisse'),
        ('3', 'OD'),
        ('4', 'Vente'),
    ]

    category = forms.ChoiceField(choices=CATEGORY_CHOICES)
    excel_file = forms.FileField()
