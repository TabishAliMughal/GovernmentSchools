from django import forms
from django.forms import ModelForm
from .models import *


class ManageProvenceCreateForm(forms.ModelForm):
    class Meta:
        model = Provence
        fields = [
            'provencename',
        ]

class ManageDivisionCreateForm(forms.ModelForm):
    class Meta:
        model = Division
        fields = [
            'divisionname',
            'provence',
        ]

class ManageDistrictCreateForm(forms.ModelForm):
    class Meta:
        model = District
        fields = [
            'districtname',
            'division',
        ]

class ManageTehsilCreateForm(forms.ModelForm):
    class Meta:
        model = Tehsil
        fields = [
            'tehsilname',
            'district',
        ]

class ManageUnionCouncilCreateForm(forms.ModelForm):
    class Meta:
        model = UnionCouncil
        fields = [
            'ucname',
            'tehsil',
        ]

class ManageQualificationCreateForm(forms.ModelForm):
    class Meta:
        model = Qualification
        fields = [
            'qualificationname',
        ]

class ManageDocumentTypeCreateForm(forms.ModelForm):
    class Meta:
        model = DocumentType
        fields = [
            'documenttype',
        ]

class ManageStaffTypeCreateForm(forms.ModelForm):
    class Meta:
        model = StaffType
        fields = [
            'type',
            'group',
        ]

class ManageRoomTypeCreateForm(forms.ModelForm):
    class Meta:
        model = RoomType
        fields = [
            'type',
        ]
