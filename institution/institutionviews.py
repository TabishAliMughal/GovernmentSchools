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


def ManageNewsCreateView(CreateView,school):
    group = CreateView.user.groups.values('name')
    school = get_object_or_404(Institution,pk=school)
    form = ManageNewsCreateForm()
    if CreateView.method == 'POST':
        data = CreateView.POST
        user_form = ManageNewsCreateForm({
            'institution' : int(school.pk) ,
            'news' : data.get('news') ,
            'date' : data.get('date'),

        })
        if user_form.is_valid:
            user_form.save()
            return redirect('institution_detail_for_admin',int(school.pk))
        else:
            return render(CreateView,'Institutions/NotValid.html',{'return':'Not Valid'})
    else:
        context = {
            'user_form' : form ,
            'school' : school ,
            'group': group ,
        }
    return render(CreateView,'News/create.html',context)


def ManageActivityCreateView(CreateView,school):
    group = CreateView.user.groups.values('name')
    school = get_object_or_404(Institution,pk=school)
    form = ManageActivityCreateForm()
    if CreateView.method == 'POST':
        data = CreateView.POST
        user_form = ManageActivityCreateForm({
            'institution' : int(school.pk) ,
            'activity_name' : data.get('activity_name') ,
            'activity_pics' : data.get('activity_pics') ,
            'Date' : data.get('Date') ,

        },CreateView.FILES)
        if user_form.is_valid:
            # print(user_form)
            user_form.save()
            return redirect('institution_detail_for_admin',int(school.pk))
        else:
            return render(CreateView,'Institutions/NotValid.html',{'return':'Not Valid'})
    else:
        context = {
            'user_form' : form ,
            'school' : school ,
            'group': group ,
        }
    return render(CreateView,'Activity/create.html',context)

def ManageNewsDeleteView(DeleteView, school, news_code):
    group = DeleteView.user.groups.values('name')
    News.objects.filter(news_code=news_code).delete()
    return redirect('institution_detail_for_admin',school)

def ManageActivityDeleteView(DeleteView, school, activity_code):
    group = DeleteView.user.groups.values('name')
    School_Activities.objects.filter(activity_code=activity_code).delete()
    return redirect('institution_detail_for_admin', school)

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

def ManageInstitutionElectricityDetailView(DetailView,electricity):
    group = DetailView.user.groups.values('name')
    electricity = get_object_or_404(InstitutionElectricityAvailiblity,pk=electricity)
    
    context = {
        'electricity' : electricity ,
        'group': group ,
    }
    return render(DetailView,'Buildings/ElectricityAvailiblity/Detail.html',context)


def ManageInstitutionFurnitureDetailView(DetailView,furniture):
    group = DetailView.user.groups.values('name')
    furniture = get_object_or_404(InstitutionFurniture,pk=furniture)
    context = {
        'furniture' : furniture ,
        'group': group ,
    }
    return render(DetailView,'Buildings/Furniture/Detail.html',context)