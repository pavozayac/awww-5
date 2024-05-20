from django import forms
from .models import Rectangle

class RectangleForm(forms.ModelForm):
    class Meta:
        model = Rectangle
        exclude = ['id', 'picture']

class PictureFilterForm(forms.Form):
    filter_tags = forms.CharField(label='Filter by tags', required=False)
    sort_date = forms.ChoiceField(choices=[('asc', 'ascending'), ('desc', 'descending')])