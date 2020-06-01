from django.shortcuts import render , get_list_or_404 , get_object_or_404 , redirect, HttpResponse
from .models import *
from institution.models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group , User
from authentication.user_handeling import unauthenticated_user, allowed_users, admin_only
from main.models import *
from .forms import *
from authentication.forms import *
import csv, io
from django.contrib import messages







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

def ManageInstitutionStaffDetailView(DetailView,school, employ):
    group = DetailView.user.groups.values('name')
    school = get_object_or_404(Institution , pk = int(school) )
    employ = get_object_or_404(Employ,pk=employ)
    context = {
        'school' :school,
        'employ' : employ ,
        'group': group ,
    }
    return render(DetailView,'Staff/Detail.html',context)

# def ManageTeachingStaffListView(ListView, school, type):
#     group = ListView.user.groups.values('name')
#     school = get_object_or_404(Institution , pk = int(school) )
#     types = StaffType.objects.all()
#     teacher = []
#     currenttype = get_object_or_404(StaffType , pk = str(type))
#     for i in Employ.objects.all():
#         if str(i.institution) == str(school) and str(i.type.pk) == str(type):
#             teacher.append(i)
#     context = {
#         'types':types, 
#         'type': currenttype,
#         'school':school ,
#         'teacher':teacher,
#         'group': group ,
#     }
#     return render(ListView,'Staff/StaffList.html',context)


# def ManageNonTeachingStaffListView(ListView, school):
#     group = ListView.user.groups.values('name')
#     school = get_object_or_404(Institution , pk = int(school) )
#     no_teacher = []
#     for i in Employ.objects.all():
#         if str(i.institution) == str(school):
#             no_teacher.append(i)
#     context = {
#         'school':school ,
#         'no_teacher':no_teacher,
#         'group': group ,
#     }
#     return render(ListView,'Staff/StaffList.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin','SchoolPrincipal'])
def ManageInstitutionStaffDeleteView(DeleteView, staff,institution):
    todelete = get_object_or_404(Employ,persionalnumber = int(staff))
    type = todelete.type.pk
    if str(todelete.user) != 'None':
        user = todelete.user.pk
        usertodelete = get_object_or_404(User, pk = int(user))
        usertodelete.delete()
    todelete.delete()
    return redirect('institution_staff_list',institution,type)

def ManageInstitutionStaffEditView(EditView, staff,institution):
    group = EditView.user.groups.values('name')
    employ = get_object_or_404(Employ, persionalnumber=int(staff))
    if EditView.method == "POST":
        user_form = ManageSchoolStaffCreateForm(EditView.POST,instance=employ)
        # if user_form.is_valid():
        # print(user_form)
        user_form.save()
        # print(institution)
        # print(employ.type)
        return redirect('institution_staff_list',institution,employ.type.pk)
    else:
        user_form = ManageSchoolStaffCreateForm(instance=employ)
        # print(user_form)
        dob = str(employ.dateofbirth)
        doa = str(employ.dateofapplication)
        doj = str(employ.dateofjoin)
        dom = str(employ.dateofmedical)
        dor = str(employ.dateofretirement)
        dojd = str(employ.dateofjoinindivision)
        dore = str(employ.dateofregularistation)
        dobed = str(employ.bedresultdate)
        # print(doa)
        context = {
            'bedresultdate': dobed, 
            'dateofregularistation': dore,
            'dateofjoinindivision': dojd,
            'dateofretirement': dor,
            'dateofmedical': dom, 
            'dateofapplication': doa,
            'dateofbirth' : dob ,
            'dateofjoin': doj ,
            'user_form': user_form ,
            'group': group ,
        }
        return render(EditView, 'Staff/Edit.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin','SchoolPrincipal'])
def ManageInstitutionStaffCreateView(CreateView,school,type):
    group = CreateView.user.groups.values('name')
    selectedtype = get_object_or_404(StaffType , pk = int(type))
    if CreateView.method == 'POST':
        ins = int(school)
        data = CreateView.POST
        nam = ''
        for i in data.get('name'):
            if i != ' ':
                nam = str(nam)+str(i.lower())
        # print(nam)
        pas = 'abc123xyz'
        form = CreateUserForm({
            'username' : nam.lower() ,
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
            'institution': ins ,
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
        # print(ProfileView.user)
        # print(i.user)
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

def staff_upload(request, school, type):
    group = request.user.groups.values('name')
    template = "Staff/upload.html"
    school = get_object_or_404(Institution , pk = int(school))
    selecttype = get_object_or_404(StaffType , pk = int(type))


    if request.method == "GET":
        return render(request, template)

    csv_file = request.FILES['file']

    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'This is not a csv file')

    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    for i in Employ.objects.all():
        if str(i.institution.pk) == str(school.pk):
            i.delete()
    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
        selectedtype = get_object_or_404(StaffType , type = column[36])
        nam = ''
        for i in column[0]:
            if i != ' ':
                nam = str(nam)+str(i.lower())
        pas = '{}@123'.format(column[5])
        form = CreateUserForm({
            'username' : nam.lower() ,
            'email' : '{}@gmail.com'.format((nam.lower())) ,
            'password1' : str(pas) , 
            'password2' : str(pas) ,
        })
        form.save()
        user = get_object_or_404(User , username = nam )
        user.groups.add(selectedtype.group.pk)

        if column[2] == "Male" or column[2] == "M":
            gen = "M"
        else:
            gen = "F"
        if column[24] == "Active" or column[24] == "A":
            sta = "A"
        else:
            sta = "I"
        if column[25] == "Yes" or column[25] == "Y":
            inter = "Y"
        else:
            inter = "N"
        created = ManageSchoolStaffCreateForm({
            'user': user.pk ,
            'name' : column[0],
            'fathername' : column[1],
            'gender' : gen,
            'designation' : column[3],
            'currentbps' : column[4],
            'persionalnumber' : column[5],
            'cnic' : column[6],
            'contact' : column[7],
            'dateofbirth' : column[8],
            'dateofapplication' : column[9],
            'dateofjoin' : column[10],
            'dateofmedical' : column[11],
            'dateofregularistation' : column[12],
            'bpsatfirstjoin' : column[13],
            'qualification' : get_object_or_404(Qualification , qualificationname = column[14]).pk ,
            'domicile' : get_object_or_404(Division , divisionname = column[15]).pk ,
            'matricpassingyear':  column[16],
            'interpassingyear':  column[17],
            'graduationyear' : column[18],
            'otheraccademics' : column[19],
            'bedpassingyear' : column[20],
            'bedresultdate' : column[21],
            'otherprofessionalqualification' : column[22],
            'biometricverified' : column[23],
            'status' : sta,
            'interdistricttransfer' : inter,
            'dateofjoinindivision' : column[26],
            'dateofretirement' : column[27],
            'remarks' : column[28],
            'uc'  : get_object_or_404(UnionCouncil , ucname = column[29]).pk ,
            'prefix' : column[30],
            'institution' : get_object_or_404(Institution , name = column[31]).pk ,
            'address' : column[32],
            'headname' : column[33],
            'head' : column[34],
            'training' : column[35],
            'type': get_object_or_404(StaffType , type = column[36]).pk ,

        })
    # print(created)
        created.save()
    context = {'staff': 'Added Successfully', 'group':group, 'school':school, 'type':selecttype }
    return render(request, 'Staff/uploaded.html', context)


def staff_download(request):
    
    items = Employ.objects.all()
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="TeachingStaff.csv"'

    writer = csv.writer(response, delimiter=',')
    fields = ( 
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
        )
    data = Employ.objects.all()
    writer = csv.DictWriter(response , fieldnames = fields)
    writer.writeheader()
    for i in data:
        writer.writerow({
            'name': i.name , 
            'fathername':i.fathername ,
            'gender': i.gender ,
            'designation':i.designation ,
            'currentbps':i.currentbps ,
            'persionalnumber':i.persionalnumber ,
            'cnic':i.cnic ,
            'contact':i.contact ,
            'dateofbirth':i.dateofbirth ,
            'dateofapplication':i.dateofapplication ,
            'dateofjoin':i.dateofjoin ,
            'dateofmedical':i.dateofmedical,
            'dateofregularistation':i.dateofregularistation,
            'bpsatfirstjoin': i.bpsatfirstjoin,
            'qualification': i.qualification,
            'domicile': i.domicile,
            'matricpassingyear': i.matricpassingyear,
            'interpassingyear': i.interpassingyear,
            'graduationyear': i.graduationyear,
            'otheraccademics': i.otheraccademics,
            'bedpassingyear': i.bedpassingyear,
            'bedresultdate': i.bedresultdate,
            'otherprofessionalqualification': i.otherprofessionalqualification,
            'biometricverified': i.biometricverified,
            'status': i.status,
            'interdistricttransfer': i.interdistricttransfer,
            'dateofjoinindivision': i.dateofjoinindivision,
            'dateofretirement': i.dateofretirement,
            'remarks': i.remarks,
            'uc': i.uc,
            'prefix': i.prefix,
            'institution': i.institution,
            'address': i.address,
            'headname': i.headname,
            'head': i.head,
            'training': i.training,
            'type' : i.type,
            })
    return response