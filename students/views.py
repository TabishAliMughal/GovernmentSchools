from django.shortcuts import render , get_list_or_404 , get_object_or_404 , redirect, HttpResponse
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group , User
from authentication.user_handeling import unauthenticated_user, allowed_users, admin_only
from main.models import *
from institution.models import *
from authentication.forms import *
import csv, io
from django.contrib import messages



@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin','SchoolPrincipal'])
def ManageStudentListView(ListView,school):
    group = ListView.user.groups.values('name')
    school = get_object_or_404(Institution , pk = int(school))
    students = []
    for i in Student.objects.all():
        if str(i.school_name.pk) == str(school.pk):
            students.append(i)
    context = {
        'types' : StaffType.objects.all() ,
        'school': school ,
        'students': students,
        'group': group ,
    }
    return render(ListView,'Students/List.html',context)


def ManageStudentDetailView(DetailView,school, gr):
    group = DetailView.user.groups.values('name')
    school = get_object_or_404(Institution,pk=school)
    student = get_object_or_404(Student, gr = gr)
    context = {
        'types' : StaffType.objects.all() ,
        'student':student,
        'school' : school ,
        'group': group ,
    }
    return render(DetailView,'Students/Detail.html',context)

def ManageStudentDeleteView(DeleteView, school, gr):
    group = DeleteView.user.groups.values('name')
    Student.objects.filter(gr=gr).delete()
    return redirect('student_list',school)


def ManageStudentEditView(EditView, school, gr):
    group = EditView.user.groups.values('name')
    school = get_object_or_404(Institution,pk=school)
    student = get_object_or_404(Student, gr=gr)

    if EditView.method == "POST":
        user_form = StudentCreateForm(EditView.POST or None, instance=student)
        if user_form.is_valid():
            user_form.save()
            return redirect('student_list')
    else:
        user_form = StudentCreateForm(instance=student)

        return render(EditView, 'Students/edit.html', {'user_form': user_form})


def ManageStudentCreateView(CreateView,school):
    group = CreateView.user.groups.values('name')
    school = get_object_or_404(Institution , pk = int(school))
    if CreateView.method == 'POST':
        data = CreateView.POST
        # school = get_object_or_404(Institution,pk=str(school))
        user_form = StudentCreateForm({
            'school_name' : int(school.pk) ,
            'gr' : data.get('gr') ,
            'name' : data.get('name') ,
            'father_name' : data.get('father_name') ,
            'gender' : data.get('gender') ,
            'father_cnic_no' : data.get('father_cnic_no') ,
            'father_contact_no' : data.get('father_contact_no') ,
            'address' : data.get('address') ,
            'Class' : data.get('Class') ,
            'date_birth' : data.get('date_birth') ,
            'date_admission' : data.get('date_admission') ,
            'date_leaving_school' : data.get('date_leaving_school') ,
            'Reason_of_leaving' : data.get('Reason_of_leaving') ,
            'religion' : data.get('religion') ,
        })
        if user_form.is_valid:
            user_form.save()
            return redirect('student_list', int(school.pk))
        else:
            context = {
        'types' : StaffType.objects.all() ,
                'return ': 'Is Not Valid'
            }
            return render(CreateView, 'Students/Created.html', context)
    else:
        # print(school)
        user_form = StudentCreateForm()
        context = {
        'types' : StaffType.objects.all() ,
            'user_form':user_form ,
            'school': school,
            'group': group ,
        } 
        return render(CreateView, 'Students/Create.html',context )


def student_upload(request, school):
    group = request.user.groups.values('name')
    template = "Students/upload.html"
    school = get_object_or_404(Institution,pk=int(school))

    prompt = {
        'order': 'Order of the CSV should be school_name, gr, name, father_name, gender, father_cnic_no, father_contact_no, address, Class,date_birth, date_admission, date_leaving_school, Reason_of_leaving, religion'
    }

    if request.method == "GET":
        return render(request, template, prompt)

    csv_file = request.FILES['file']

    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'This is not a csv file')

    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    for i in Student.objects.all():
        if str(i.school_name.pk) == str(school.pk):
            i.delete()
    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
        if column[3] == "Male" or column[3] == "M":
            gen = "M"
        else:
            gen = "F"
        created = StudentCreateForm({
            'school_name' : int(school.pk) ,
            'gr' : column[0] ,
            'name' : column[1] ,
            'father_name' : column[2] ,
            'gender' : gen ,
            'father_cnic_no' : column[4] ,
            'father_contact_no' : column[5] ,
            'address' : column[6] ,
            'Class' :  get_object_or_404(Class , classes = column[7]).pk ,
            'date_birth' :  column[8] ,
            'date_admission' :  column[9] ,
            'date_leaving_school' :  column[10] ,
            'Reason_of_leaving' :  column[ 11] ,
            'religion' :  column[12] ,

        })
    # print(created)
        created.save()
    context = {
        'types' : StaffType.objects.all() ,'student': 'Added Successfully', 'group':group, 'school':school }
    return render(request, 'Students/uploaded.html', context)


def student_download(request):
    
    items = Student.objects.all()
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="students.csv"'

    writer = csv.writer(response, delimiter=',')
    fields = ( 
        'gr',
        'name',
        'father_name',
        'gender',
        'father_cnic_no',
        'father_contact_no',
        'address','Class',
        'date_birth',
        'date_admission',
        'date_leaving_school',
        'Reason_of_leaving',
        'religion',
        )
    data = Student.objects.all()
    writer = csv.DictWriter(response , fieldnames = fields)
    writer.writeheader()
    for i in data:
        writer.writerow({'gr': i.gr , 'name':i.name ,'father_name':i.father_name ,'gender': i.gender ,'father_cnic_no':i.father_cnic_no ,'father_contact_no':i.father_contact_no ,'address':i.address ,'Class':i.Class ,'date_birth':i.date_birth ,'date_admission':i.date_admission ,'date_leaving_school':i.date_leaving_school ,'Reason_of_leaving':i.Reason_of_leaving ,'religion':i.religion})
    return response


