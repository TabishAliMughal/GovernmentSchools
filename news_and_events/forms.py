from django import forms
from django.forms import ModelForm
from .models import *

class ManageNewsCreateForm(forms.ModelForm):
    class Meta:
        model = News
        fields = [
            'institution',
            'news',
            'date',
        ]


class ManageActivityCreateForm(forms.ModelForm):
    class Meta:
        model = School_Activities
        fields = [
            'institution',
            'activity_name',
            'activity_pics',
            'Date',
        ]