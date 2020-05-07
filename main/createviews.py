from django.shortcuts import render , get_list_or_404 , get_object_or_404 , redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group , User
from authentication.user_handeling import unauthenticated_user, allowed_users, admin_only
from .models import *
from .forms import *



def ManageProvenceCreateView(CreateView):
    group = CreateView.user.groups.values('name')
    if CreateView.method == 'POST':
        form = ManageProvenceCreateForm(CreateView.POST)
        if form.is_valid:
            form.save()
            return redirect('provence_list')
        else:
            return render(CreateView,'Error/NotValid.html')
    else:
        form = ManageProvenceCreateForm()
        context = {
            'name' : 'Provence' ,
            'form' : form ,
            'group': group ,
        }
        return render(CreateView,'Main/Provence/Create.html',context)

def ManageDivisionCreateView(CreateView):
    group = CreateView.user.groups.values('name')
    if CreateView.method == 'POST':
        form = ManageDivisionCreateForm(CreateView.POST)
        if form.is_valid:
            form.save()
            return redirect('division_list')
        else:
            return render(CreateView,'Error/NotValid.html')
    else:
        form = ManageDivisionCreateForm()
        context = {
            'name' : 'Division' ,
            'form' : form ,
            'group': group ,
        }
        return render(CreateView,'Main/Division/Create.html',context)

def ManageDistrictCreateView(CreateView):
    group = CreateView.user.groups.values('name')
    if CreateView.method == 'POST':
        form = ManageDistrictCreateForm(CreateView.POST)
        if form.is_valid:
            form.save()
            return redirect('district_list')
        else:
            return render(CreateView,'Error/NotValid.html')
    else:
        form = ManageDistrictCreateForm()
        context = {
            'name' : 'District' ,
            'form' : form ,
            'group': group ,
        }
        return render(CreateView,'Main/District/Create.html',context)

def ManageTehsilCreateView(CreateView):
    group = CreateView.user.groups.values('name')
    if CreateView.method == 'POST':
        form = ManageTehsilCreateForm(CreateView.POST)
        if form.is_valid:
            form.save()
            return redirect('tehsil_list')
        else:
            return render(CreateView,'Error/NotValid.html')
    else:
        form = ManageTehsilCreateForm()
        context = {
            'name' : 'Tehsil' ,
            'form' : form ,
            'group': group ,
        }
        return render(CreateView,'Main/Tehsil/Create.html',context)

def ManageUnionCouncilCreateView(CreateView):
    group = CreateView.user.groups.values('name')
    if CreateView.method == 'POST':
        form = ManageUnionCouncilCreateForm(CreateView.POST)
        if form.is_valid:
            form.save()
            return redirect('unioncouncil_list')
        else:
            return render(CreateView,'Error/NotValid.html')
    else:
        form = ManageUnionCouncilCreateForm()
        context = {
            'name' : 'UnionCouncil' ,
            'form' : form ,
            'group': group ,
        }
        return render(CreateView,'Main/UnionCouncil/Create.html',context)

def ManageQualificationCreateView(CreateView):
    group = CreateView.user.groups.values('name')
    if CreateView.method == 'POST':
        form = ManageQualificationCreateForm(CreateView.POST)
        if form.is_valid:
            form.save()
            return redirect('qualification_list')
        else:
            return render(CreateView,'Error/NotValid.html')
    else:
        form = ManageQualificationCreateForm()
        context = {
            'name' : 'Qualification' ,
            'form' : form ,
            'group': group ,
        }
        return render(CreateView,'Main/Qualification/Create.html',context)

def ManageDocumentTypeCreateView(CreateView):
    group = CreateView.user.groups.values('name')
    if CreateView.method == 'POST':
        form = ManageDocumentTypeCreateForm(CreateView.POST)
        if form.is_valid:
            form.save()
            return redirect('documenttype_list')
        else:
            return render(CreateView,'Error/NotValid.html')
    else:
        form = ManageDocumentTypeCreateForm()
        context = {
            'name' : 'DocumentType' ,
            'form' : form ,
            'group': group ,
        }
        return render(CreateView,'Main/DocumentType/Create.html',context)

def ManageStaffTypeCreateView(CreateView):
    group = CreateView.user.groups.values('name')
    if CreateView.method == 'POST':
        form = ManageStaffTypeCreateForm(CreateView.POST)
        if form.is_valid:
            form.save()
            return redirect('stafftype_list')
        else:
            return render(CreateView,'Error/NotValid.html')
    else:
        form = ManageStaffTypeCreateForm()
        context = {
            'name' : 'StaffType' ,
            'form' : form ,
            'group': group ,
        }
        return render(CreateView,'Main/StaffType/Create.html',context)

def ManageRoomTypeCreateView(CreateView):
    group = CreateView.user.groups.values('name')
    if CreateView.method == 'POST':
        form = ManageRoomTypeCreateForm(CreateView.POST)
        if form.is_valid:
            form.save()
            return redirect('roomtype_list')
        else:
            return render(CreateView,'Error/NotValid.html')
    else:
        form = ManageRoomTypeCreateForm()
        context = {
            'name' : 'RoomType' ,
            'form' : form ,
            'group': group ,
        }
        return render(CreateView,'Main/RoomType/Create.html',context)

