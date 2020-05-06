from django.shortcuts import render , get_list_or_404 , get_object_or_404 , redirect
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group , User
from authentication.user_handeling import unauthenticated_user, allowed_users, admin_only
from user.teacherviews import *
from main.models import *
from .forms import *
from authentication.forms import *



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
def ManageAllInstitutionsDetailForAdminView(DetailView,school):
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

@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin'])
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

@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin'])
def ManageSchoolStaffCreateView(CreateView,type):
    group = CreateView.user.groups.values('name')
    selectedtype = get_object_or_404(StaffType , pk = int(type))
    if CreateView.method == 'POST':
        # user_form = ManageSchoolStaffCreateForm(CreateView.POST)
        data = CreateView.POST
        pas = '{}{}'.format(data.get('name'),data.get('persionalnumber'))
        form = CreateUserForm({
            'username' : data.get('name') ,
            'email' : '{}@gmail.com'.format(data.get('name')) ,
            'password1' : pas , 
            'password2' : pas ,
        })
        form.save()
        user = get_object_or_404(User , username = data.get('name') )
        user.groups.add(selectedtype.group.pk)
        user_form = ManageSchoolStaffCreateForm({
            'user' : user.pk ,
            'name': data.get('name') ,
            'fathername': data.get('fathername') ,
            'gender': data.get('gender') ,
            'designation': data.get('designation') ,
            'currentbps': data.get('currentbps') ,
            'persionalnumber': data.get('persionalnumber') ,
            'cnic': data.get('cnic') ,
            'contact': data.get('contact') ,
            'dateofbirth': data.get('dateofbirth') ,
            'dateofapplication': data.get('dateofapplication') ,
            'dateofjoin': data.get('dateofjoin') ,
            'dateofmedical': data.get('dateofmedical') ,
            'dateofregularistation': data.get('dateofregularistation') ,
            'bpsatfirstjoin': data.get('bpsatfirstjoin') ,
            'qualification': data.get('qualification') ,
            'domicile': data.get('domicile') ,
            'matricpassingyear': data.get('matricpassingyear') ,
            'interpassingyear': data.get('interpassingyear') ,
            'graduationyear': data.get('graduationyear') ,
            'otheraccademics': data.get('otheraccademics') ,
            'bedpassingyear': data.get('bedpassingyear') ,
            'bedresultdate': data.get('bedresultdate') ,
            'otherprofessionalqualification': data.get('otherprofessionalqualification') ,
            'biometricverified': data.get('biometricverified') ,
            'status': data.get('status') ,
            'interdistricttransfer': data.get('interdistricttransfer') ,
            'dateofjoinindivision': data.get('dateofjoinindivision') ,
            'dateofretirement': data.get('dateofretirement') ,
            'remarks': data.get('remarks') ,
            'uc': data.get('uc') ,
            'prefix': data.get('prefix') ,
            'institution': data.get('institution') ,
            'address': data.get('address') ,
            'headname': data.get('headname') ,
            'head': data.get('head') ,
            'training': data.get('training') ,
            'type': (selectedtype.pk) ,
        })
        if user_form.is_valid():
            user_form.save()
            context = {
                'return': 'Has Been Added Successfully'
            } 
            return render(CreateView, 'Staff/Created.html', context)
        # else:
        #     context = {
        #         'return ': 'Is Not Valid'
        #     }
        #     return render(CreateView, 'Staff/Created.html', context)
    else:
        user_form = ManageSchoolStaffCreateForm()
        context = {
            'type':selectedtype ,
            'user_form':user_form ,
            'group': group ,
        } 
        return render(CreateView, 'Staff/Create.html',context )

@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin'])
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

