from django.shortcuts import render , get_object_or_404 , get_list_or_404 , redirect
from institution.models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group , User
from authentication.user_handeling import unauthenticated_user, allowed_users, admin_only



def ManageMainView(DisplayView):
    group = DisplayView.user.groups.values('name')
    institutions = Institution.objects.all()
    context = {
        'institutions': institutions ,
        'group': group ,
    }
    return render(DisplayView,'Main/Main.html',context)

def ManageInstitutionDetailForAllView(DetailView,school):
    group = DetailView.user.groups.values('name')
    school = get_object_or_404(Institution,pk=school)
    context = {
        'school' : school ,
        'group': group ,
    }
    return render(DetailView,'Main/InstituteDetail.html',context)