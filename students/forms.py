from django import forms
from django.forms import ModelForm
from .models import *

class StudentCreateForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = {
            'school_name',
            'gr',
            'name',
            'father_name',
            'gender',
            'father_cnic_no',
            'father_contact_no',
            'address',
            'Class',
            'date_birth',
            'date_admission',
            'date_leaving_school',
            'Reason_of_leaving',
            'religion',
        }