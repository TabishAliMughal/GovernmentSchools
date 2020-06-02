from django.shortcuts import render , get_list_or_404 , get_object_or_404 , redirect
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group , User
from authentication.user_handeling import unauthenticated_user, allowed_users, admin_only
from main.models import *
from news_and_events.models import *
from news_and_events.forms import *
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
@allowed_users(allowed_roles=['Admin','SchoolPrincipal'])
def ManageAllInstitutionsDetailForAdminView(DetailView,school):
    group = DetailView.user.groups.values('name')
    school = get_object_or_404(Institution,pk=school)
    news = []
    for i in News.objects.all():
        if str(i.institution.pk) == str(school.pk):
            news.append(i)
    activities = []
    picture = []
    for j in School_Activities.objects.all():
        if str(j.institution.pk) == str(school.pk):
            activities.append({
                'activity_code' : j.activity_code ,
                'institution' : j.institution ,
                'activity_name' : j.activity_name ,
                'activity_pics' : str(j.activity_pics)[7:] ,
                'Date' : j.Date ,
            })
            # print(j.activity_pics)
            # print( j.activity_pics)
            # picture = (str(j.activity_pics)[7:])
            # picture.append(str(j.activity_pics)[7:])
    # for i in activities:
    # print(picture)
    
    context = {
        'picture': picture, 
        'activities': activities,
        'news':news,
        'school' : school ,
        'group': group ,
    }
    return render(DetailView,'Institutions/HeadSelect.html',context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin'])
def ManageInstututeCreateView(CreateView):
    group = CreateView.user.groups.values('name')
    if CreateView.method == 'POST':
        # sel = get_object_or_404(Group , name = '')
        data = CreateView.POST
        semis_id = data.get('semis_id')
        name = data.get('name')
        nam = ''
        for i in name:
            if i != ' ':
                nam = str(nam)+str((i.lower()))
        password = str('{}@123'.format(str(semis_id)))
        form = UserCreationForm({
            'username' : nam ,
            'email' : '{}@gmail.com'.format(nam) ,
            'password1' : password ,
            'password2' : password ,
        })
        save = form.save()
        selgroup = Group.objects.get(name='SchoolPrincipal')
        save.groups.add(selgroup)
        user_form = ManageInstituteCreateForm({
            'semis_id' : data.get('semis_id') ,
            'name' : data.get('name') ,
            'unioncouncil' : data.get('unioncouncil') ,
            'user' : save ,
        })
        if user_form.is_valid():
            user_form.save()
            context = {
                'return': 'Has Been Added Successfully' ,
                'group': group ,
            } 
            return render(CreateView, 'Institutions/Created.html', context)
        else:
            context = {
                'return ': 'Is Not Valid' ,
                'group': group ,
            }
            return render(CreateView, 'Institutions/Created.html', context)
    else:
        user_form = ManageInstituteCreateForm()
        context = {
            'user_form':user_form ,
            'group': group ,
        } 
        return render(CreateView, 'Institutions/Create.html',context )
