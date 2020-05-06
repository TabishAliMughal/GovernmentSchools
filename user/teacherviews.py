from django.shortcuts import render , get_list_or_404 , get_object_or_404 , redirect
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group , User
from authentication.user_handeling import unauthenticated_user, allowed_users, admin_only




def ManageTeacherProfileView(ProfileView,user):
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
    return render(ProfileView,'Users/Teacher/Profile.html',context)

def ManageTeacherDocumentsView(DocumentView,teacher):
    group = DocumentView.user.groups.values('name')
    picture = []
    for i in EmployDocuments.objects.all():
        if str(i.employ.pk) == str(teacher):
            pic = str(i.picture)[7:]
            picture.append({'url':pic,'type':i.documenttype})
    context = {
        'picture':picture ,
        'group': group ,
    }
    return render(DocumentView,'Users/Teacher/Documents.html',context)






