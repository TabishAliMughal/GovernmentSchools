from django.shortcuts import render , get_list_or_404 , get_object_or_404 , redirect
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group , User
from authentication.user_handeling import unauthenticated_user, allowed_users, admin_only
from main.models import *
from .forms import *
from authentication.forms import *







@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin','SchoolPrincipal'])
def ManageInstitutionStaffTypeSelectView(SelectView,school):
    group = SelectView.user.groups.values('name')
    types = StaffType.objects.all()
    school = get_object_or_404(Institution , pk = int(school) )
    context = {
        'types' : types ,
        'school' : school ,
        'group': group ,
    }
    return render(SelectView,'Staff/StaffTypeSelect.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin','SchoolPrincipal'])
def ManageInstitutionStaffListView(ProfileView,school,type):
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
    return render(ProfileView,'Staff/StaffList.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin','SchoolPrincipal'])
def ManageInstitutionStaffCreateView(CreateView,school,type):
    group = CreateView.user.groups.values('name')
    selectedtype = get_object_or_404(StaffType , pk = int(type))
    if CreateView.method == 'POST':
        data = CreateView.POST
        nam = ''
        for i in data.get('name'):
            if i != ' ':
                nam = str(nam)+str(i)
        pas = 'abc123xyz'
        form = CreateUserForm({
            'username' : nam ,
            'email' : '{}@gmail.com'.format((nam.lower())) ,
            'password1' : str(pas) , 
            'password2' : str(pas) ,
        })
        form.save()
        user = get_object_or_404(User , username = nam )
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
            'institution': school ,
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
        else:
            context = {
                'return ': 'Is Not Valid'
            }
            return render(CreateView, 'Staff/Created.html', context)
    else:
        user_form = ManageSchoolStaffCreateForm()
        context = {
            'type':selectedtype ,
            'user_form':user_form ,
            'group': group ,
        } 
        return render(CreateView, 'Staff/Create.html',context )

@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin','SchoolPrincipal','Teachers'])
def ManageStaffProfileView(ProfileView,user):
    group = ProfileView.user.groups.values('name')
    teacher = []
    abc = get_object_or_404(Employ , user = int(user))
    for i in Employ.objects.all():
        if str(i.user.pk) == str(user):
            teacher = i
    if teacher == '':
        teacher = 'No'
    context = {
        'abc':abc,
        'teacher':teacher,
        'group': group ,
    }
    return render(ProfileView,'Staff/Profile.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin','SchoolPrincipal','Teachers'])
def ManageStaffDocumentsView(DocumentView,teacher):
    group = DocumentView.user.groups.values('name')
    picture = []
    for i in EmployDocuments.objects.all():
        if str(i.employ.pk) == str(teacher):
            pic = str(i.picture)[7:]
            picture.append({'url':pic,'type':i.documenttype})
    context = {
        'staff' : teacher ,
        'picture': picture ,
        'group': group ,
    }
    return render(DocumentView,'Staff/Documents/List.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['SchoolPrincipal'])
def ManagePrincipleProfileView(ProfileView,user):
    for i in Institution.objects.all():
        print(ProfileView.user)
        print(i.user)
        if str(ProfileView.user) == str(i.user):
            return redirect('institution_detail_for_admin',i.pk)

@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin','SchoolPrincipal'])
def ManageStaffDocumentsCreateView(CreateView,teacher):
    group = CreateView.user.groups.values('name')
    teacher = get_object_or_404(Employ,pk=teacher)
    form = ManageStaffDocumentsCreateForm()
    if CreateView.method == 'POST':
        data = CreateView.POST
        user_form = ManageStaffDocumentsCreateForm({
            'documenttype' : data.get('documenttype') ,
            'employ' : teacher.pk ,
        },CreateView.FILES)
        if user_form.is_valid:
            user_form.save()
            return redirect('staff_documents',int(teacher.pk))
        else:
            return render(CreateView,'Staff/NotValid.html',{'return':'Not Valid'})
    else:
        context = {
            'form' : form ,
            'teacher' : teacher ,
            'group': group ,
        }
    return render(CreateView,'Staff/Documents/Create.html',context)
