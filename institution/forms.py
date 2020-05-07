from django import forms
from django.forms import ModelForm
from .models import *

class ManageInstituteCreateForm(forms.ModelForm):
    class Meta:
        model = Institution
        fields = [
            'semis_id',
            'name',
            'unioncouncil',
            'user',
        ]

class InstitutionRoomsCreateForm(forms.ModelForm):
    class Meta:
        model = InstitutionRooms
        fields = [
            'institution' ,
            'roomtype' ,
            'therefor' ,
            'rooms' ,
        ]

class InstitutionBoundaryWallCreateForm(forms.ModelForm):
    class Meta:
        model = InstitutionBoundaryWall
        fields = [
            'institution' ,
            'available' ,
            'ifyes' ,
        ]

class InstitutionBuildingConditionCreateForm(forms.ModelForm):
    class Meta:
        model = InstitutionBuildingCondition
        fields = [
            'institution' ,
            'condition' ,
            'ifrepairable' ,
        ]

class InstitutionAreaCreateForm(forms.ModelForm):
    class Meta:
        model = InstitutionArea
        fields = [
            'institution' ,
            'length' ,
            'width' ,
        ]

class InstitutionWaterAvailiblityCreateForm(forms.ModelForm):
    class Meta:
        model = InstitutionWaterAvailiblity
        fields = [
            'institution' ,
            'available' ,
            'availabletype' ,
        ]

class InstitutionROPlantAvailiblityCreateForm(forms.ModelForm):
    class Meta:
        model = InstitutionROPlantAvailiblity
        fields = [
            'institution' ,
            'available' ,
            'type' ,
            'qty' ,
        ]

class InstitutionWaterDispenserAvailiblityCreateForm(forms.ModelForm):
    class Meta:
        model = InstitutionWaterDispenserAvailiblity
        fields = [
            'institution' ,
            'available' ,
            'type' ,
            'qty' ,
        ]

class InstitutionPlayGroundCreateForm(forms.ModelForm):
    class Meta:
        model = InstitutionPlayGround
        fields = [
            'institution' ,
            'available' ,
            'type' ,
        ]

class InstitutionPlantationCreateForm(forms.ModelForm):
    class Meta:
        model = InstitutionPlantation
        fields = [
            'institution' ,
            'available' ,
            'qtyoftrees' ,
            'qtyofplants' ,
        ]

class InstitutionToiletAvailiblityCreateForm(forms.ModelForm):
    class Meta:
        model = InstitutionToiletAvailiblity
        fields = [
            'institution' ,
            'available' ,
            'qty' ,
            'functionalqty' ,
        ]

class InstitutionWiringAvailiblityCreateForm(forms.ModelForm):
    class Meta:
        model = InstitutionWiringAvailiblity
        fields = [
            'institution' ,
            'available' ,
            'condition' ,
        ]

class InstitutionPlumbingAvailiblityCreateForm(forms.ModelForm):
    class Meta:
        model = InstitutionPlumbingAvailiblity
        fields = [
            'institution' ,
            'available' ,
            'condition' ,
        ]

class InstitutionSenitaryAvailiblityCreateForm(forms.ModelForm):
    class Meta:
        model = InstitutionSenitaryAvailiblity
        fields = [
            'institution' ,
            'available' ,
        ]

class InstitutionElectricityAvailiblityCreateForm(forms.ModelForm):
    class Meta:
        model = InstitutionElectricityAvailiblity
        fields = [
            'institution' ,
            'available' ,
            'meter' ,
            'meterno' ,
            'consumerno' ,
            'contactaccnp' ,
            'kunda' ,
            'solar' ,
            'solarqty' ,
        ]

class InstitutionFurnitureCreateForm(forms.ModelForm):
    class Meta:
        model = InstitutionFurniture
        fields = [
            'institution' ,
            'therefor' ,
            'dualdeskqty' ,
            'chairsqty' ,
            'tablesqty' ,
            'shelvesqty' ,
            'lockersqty' ,
            'cupboardqty' ,
            'others' ,
        ]
