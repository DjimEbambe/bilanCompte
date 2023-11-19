# forms.py
from django import forms


class Form(forms.Form):
    CATEGORY_CHOICES = [
        ('option1', 'Option 1'),
        ('option2', 'Option 2'),
        # Add other choices as needed
    ]

    category = forms.ChoiceField(choices=CATEGORY_CHOICES)
    excel_file = forms.FileField()
