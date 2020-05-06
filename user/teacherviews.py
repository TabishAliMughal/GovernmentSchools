from django.shortcuts import render , get_list_or_404 , get_object_or_404 , redirect
from .models import *



def ManageTeacherProfileView(ProfileView,user):
    group = ProfileView.user.groups.values('name')
    teacher = get_object_or_404(Employ , user = int(user))
    context = {
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