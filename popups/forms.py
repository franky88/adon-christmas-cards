from django import forms
from .models import PopUp, Theme
from django.forms import widgets
from django_summernote.widgets import SummernoteWidget


class PopUpForms(forms.ModelForm):
    class Meta:
        model = PopUp
        fields = [
            'business_name',
            'content',
            'title',
            'reinstatement',
            'theme'
        ]
        # widgets = {
        #     'content': SummernoteWidget(attrs={'class': 'form-control', 'summernote': {'width': '100%', 'height': '400px'}})
        # }
        widgets = {
            'content': widgets.TextInput(attrs={'rows': '5'}),
            'reinstatement': widgets.TextInput(attrs={'rows': '5'}),
        }
