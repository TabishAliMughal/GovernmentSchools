from django.shortcuts import render , get_list_or_404 , get_object_or_404 , redirect
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group , User
from authentication.user_handeling import unauthenticated_user, allowed_users, admin_only
from user.teacherviews import *
from main.models import *
from .forms import *



@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin'])
def ManageAllInstitutionsListView(ListView):
    group = ListView.user.groups.values('name')
    schools = Institution.objects.all()
    context = {
        'schools' : schools ,
        'group': group ,
    }
    return render(ListView,'Institutions/List.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin'])
def ManageAllInstitutionsDetailView(DetailView,school):
    group = DetailView.user.groups.values('name')
    school = get_object_or_404(Institution,pk=school)
    context = {
        'school' : school ,
        'group': group ,
    }
    return render(DetailView,'Institutions/HeadSelect.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin'])
def ManageInstitutionStaffTypeSelectView(SelectView,school):
    group = SelectView.user.groups.values('name')
    types = StaffType.objects.all()
    school = get_object_or_404(Institution , pk = int(school) )
    context = {
        'types' : types ,
        'school' : school ,
        'group': group ,
    }
    return render(SelectView,'Institutions/StaffTypeSelect.html',context)

def ManageSchoolStaffListView(ProfileView,school,type):
    group = ProfileView.user.groups.values('name')
    school = get_object_or_404(Institution , pk = int(school) )
    types = StaffType.objects.all()
    teacher = []
    currenttype = get_object_or_404(StaffType , pk = str(type))
    for i in Employ.objects.all():
        if str(i.institution) == str(school) and str(i.type.pk) == str(type):
            teacher.append(i)
    context = {
        'type' : currenttype ,
        'types' : types ,
        'school':school ,
        'teacher':teacher,
        'group': group ,
    }
    return render(ProfileView,'Institutions/StaffList.html',context)

def ManageInstututeCreateView(CreateView):
    if CreateView.method == 'POST':
        user_form = ManageInstituteCreateForm(CreateView.POST)
        if user_form.is_valid():
            user_form.save()
            context = {
                'return': 'Has Been Added Successfully'
            } 
            return render(CreateView, 'Institutions/Created.html', context)
        else:
            context = {
                'return ': 'Is Not Valid'
            }
            return render(CreateView, 'Institutions/Created.html', context)
    else:
        user_form = ManageInstituteCreateForm()
        context = {
            'user_form':user_form ,
        } 
        return render(CreateView, 'Institutions/Create.html',context )

