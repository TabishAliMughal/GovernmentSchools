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
        'school': school ,
        'news': news,
        'group': group ,
    }
    return render(ListView,'News/List.html',context)