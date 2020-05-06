from django import forms
from django.forms import ModelForm
from .models import *


class ManageInstituteCreateForm(forms.ModelForm):
    class Meta:
        model = Institution
        fields = {
            'semis_id',
            'name',
        }