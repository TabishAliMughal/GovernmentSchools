from django.shortcuts import render , get_list_or_404 , get_object_or_404 , redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group , User
from authentication.user_handeling import unauthenticated_user, allowed_users, admin_only
from .models import *
from .forms import *



def ManageProvenceListView(ListView):
    group = ListView.user.groups.values('name')
    provence = Provence.objects.all()
    context = {
        'types' : StaffType.objects.all() ,
        'name' : 'Provences' ,
        'provence': provence ,
        'group': group ,
    }
    return render(ListView,'Main/Provence/List.html',context)

def ManageDivisionListView(ListView):
    group = ListView.user.groups.values('name')
    division = Division.objects.all()
    context = {
        'types' : StaffType.objects.all() ,
        'name' : 'Divisions' ,
        'division': division ,
        'group': group ,
    }
    return render(ListView,'Main/Division/List.html',context)

def ManageDistrictListView(ListView):
    group = ListView.user.groups.values('name')
    district = District.objects.all()
    context = {
        'types' : StaffType.objects.all() ,
        'name' : 'Districts' ,
        'district': district ,
        'group': group ,
    }
    return render(ListView,'Main/District/List.html',context)

def ManageTehsilListView(ListView):
    group = ListView.user.groups.values('name')
    tehsil = Tehsil.objects.all()
    context = {
        'types' : StaffType.objects.all() ,
        'name' : 'Tehsils' ,
        'tehsil': tehsil ,
        'group': group ,
    }
    return render(ListView,'Main/Tehsil/List.html',context)

def ManageUnionCouncilListView(ListView):
    group = ListView.user.groups.values('name')
    unioncouncil = UnionCouncil.objects.all()
    context = {
        'types' : StaffType.objects.all() ,
        'name' : 'UnionCouncils' ,
        'unioncouncil': unioncouncil ,
        'group': group ,
    }
    return render(ListView,'Main/UnionCouncil/List.html',context)

def ManageQualificationListView(ListView):
    group = ListView.user.groups.values('name')
    qualification = Qualification.objects.all()
    context = {
        'types' : StaffType.objects.all() ,
        'name' : 'Qualifications' ,
        'qualification': qualification ,
        'group': group ,
    }
    return render(ListView,'Main/Qualification/List.html',context)

def ManageDocumentTypeListView(ListView):
    group = ListView.user.groups.values('name')
    documentType = DocumentType.objects.all()
    context = {
        'types' : StaffType.objects.all() ,
        'name' : 'DocumentTypes' ,
        'documentType': documentType ,
        'group': group ,
    }
    return render(ListView,'Main/DocumentType/List.html',context)

def ManageStaffTypeListView(ListView):
    group = ListView.user.groups.values('name')
    stafftype = StaffType.objects.all()
    context = {
        'types' : StaffType.objects.all() ,
        'name' : 'StaffTypes' ,
        'stafftype': stafftype ,
        'group': group ,
    }
    return render(ListView,'Main/StaffType/List.html',context)

def ManageRoomTypeListView(ListView):
    group = ListView.user.groups.values('name')
    roomtype = RoomType.objects.all()
    context = {
        'types' : StaffType.objects.all() ,
        'name' : 'RoomTypes' ,
        'roomtype': roomtype ,
        'group': group ,
    }
    return render(ListView,'Main/RoomType/List.html',context)