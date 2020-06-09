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

# Create your views here.

def ManageNewsListView(ListView,school):
    group = ListView.user.groups.values('name')
    school = get_object_or_404(Institution , pk = int(school))
    news = []
    for i in News.objects.all():
        if str(i.institution.pk) == str(school.pk):
            news.append(i)
    context = {
        'types' : StaffType.objects.all() ,
        'school': school ,
        'news': news,
        'group': group ,
    }
    return render(ListView,'News/List.html',context)


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
