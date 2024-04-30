from django import forms
from .models import Rectangle

class RectangleForm(forms.ModelForm):
    class Meta:
        model = Rectangle
        exclude = ['id', 'picture']