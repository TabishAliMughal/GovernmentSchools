from django import forms
from django.forms import ModelForm
from .models import *


class ManageSchoolStaffCreateForm(forms.ModelForm):
    class Meta:
        model = Employ
        fields = {
            'user',
            'name',
            'fathername',
            'gender',
            'designation',
            'currentbps',
            'persionalnumber',
            'cnic',
            'contact',
            'dateofbirth',
            'dateofapplication',
            'dateofjoin',
            'dateofmedical',
            'dateofregularistation',
            'bpsatfirstjoin',
            'qualification',
            'domicile',
            'matricpassingyear',
            'interpassingyear',
            'graduationyear',
            'otheraccademics',
            'bedpassingyear',
            'bedresultdate',
            'otherprofessionalqualification',
            'biometricverified',
            'status',
            'interdistricttransfer',
            'dateofjoinindivision',
            'dateofretirement',
            'remarks',
            'uc',
            'prefix',
            'institution',
            'address',
            'headname',
            'head',
            'training',
            'type',
        }

class ManageStaffDocumentsCreateForm(forms.ModelForm):
    class Meta:
        model = EmployDocuments
        fields = [
            'code',
            'documenttype' ,
            'employ' ,
            'picture' ,
        ]