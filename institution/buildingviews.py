from django.shortcuts import render , get_list_or_404 , get_object_or_404 , redirect
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group , User
from authentication.user_handeling import unauthenticated_user, allowed_users, admin_only
from main.models import *
from .forms import *
from authentication.forms import *




@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin','SchoolPrincipal'])
def ManageInstitutionBuildingSelectView(SelectView,school):
    group = SelectView.user.groups.values('name')
    school = get_object_or_404(Institution , pk = int(school))
    Rooms = []
    for i in InstitutionRooms.objects.all():
        if str(i.institution.pk) == str(school.pk):
            Rooms.append(i)
    BoundaryWall = []
    for i in InstitutionBoundaryWall.objects.all():
        if str(i.institution.pk) == str(school.pk):
            BoundaryWall.append(i)
    BuildingCondition = []
    for i in InstitutionBuildingCondition.objects.all():
        if str(i.institution.pk) == str(school.pk):
            BuildingCondition.append(i)
    Area = []
    for i in InstitutionArea.objects.all():
        if str(i.institution.pk) == str(school.pk):
            Area.append(i)
    WaterAvailiblity = []
    for i in InstitutionWaterAvailiblity.objects.all():
        if str(i.institution.pk) == str(school.pk):
            WaterAvailiblity.append(i)
    ROPlantAvailiblity = []
    for i in InstitutionROPlantAvailiblity.objects.all():
        if str(i.institution.pk) == str(school.pk):
            ROPlantAvailiblity.append(i)
    WaterDispenserAvailiblity = []
    for i in InstitutionWaterDispenserAvailiblity.objects.all():
        if str(i.institution.pk) == str(school.pk):
            WaterDispenserAvailiblity.append(i)
    PlayGround = []
    for i in InstitutionPlayGround.objects.all():
        if str(i.institution.pk) == str(school.pk):
            PlayGround.append(i)
    Plantation = []
    for i in InstitutionPlantation.objects.all():
        if str(i.institution.pk) == str(school.pk):
            Plantation.append(i)
    ToiletAvailiblity = []
    for i in InstitutionToiletAvailiblity.objects.all():
        if str(i.institution.pk) == str(school.pk):
            ToiletAvailiblity.append(i)
    WiringAvailiblity = []
    for i in InstitutionWiringAvailiblity.objects.all():
        if str(i.institution.pk) == str(school.pk):
            WiringAvailiblity.append(i)
    SenitaryAvailiblity = []
    for i in InstitutionSenitaryAvailiblity.objects.all():
        if str(i.institution.pk) == str(school.pk):
            SenitaryAvailiblity.append(i)
    PlumbingAvailiblity = []
    for i in InstitutionPlumbingAvailiblity.objects.all():
        if str(i.institution.pk) == str(school.pk):
            PlumbingAvailiblity.append(i)
    ElectricityAvailiblity = []
    for i in InstitutionElectricityAvailiblity.objects.all():
        if str(i.institution.pk) == str(school.pk):
            ElectricityAvailiblity.append(i)
    Furniture = []
    for i in InstitutionFurniture.objects.all():
        if str(i.institution.pk) == str(school.pk):
            Furniture.append(i)
    context = {
        'Rooms' : Rooms ,
        'BoundaryWall' : BoundaryWall ,
        'BuildingCondition' : BuildingCondition ,
        'Area' : Area ,
        'WaterAvailiblity' : WaterAvailiblity ,
        'ROPlantAvailiblity' : ROPlantAvailiblity ,
        'WaterDispenserAvailiblity' : WaterDispenserAvailiblity ,
        'PlayGround' : PlayGround ,
        'Plantation' : Plantation ,
        'ToiletAvailiblity' : ToiletAvailiblity ,
        'WiringAvailiblity' : WiringAvailiblity ,
        'PlumbingAvailiblity' : PlumbingAvailiblity ,
        'SenitaryAvailiblity' : SenitaryAvailiblity ,
        'ElectricityAvailiblity' : ElectricityAvailiblity ,
        'Furniture' : Furniture ,
        'school' : school ,
        'group': group ,
    }
    return render(SelectView,'Institutions/Building.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin','SchoolPrincipal'])
def ManageInstitutionBuildingSelectToAddView(SelectView,school):
    group = SelectView.user.groups.values('name')
    school = get_object_or_404(Institution,pk=school)
    context = {
        'school' : school ,
        'group': group ,
    }
    return render(SelectView,'Buildings/Select.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin','SchoolPrincipal'])
def ManageInstitutionRoomCreateView(CreateView,school):
    group = CreateView.user.groups.values('name')
    school = get_object_or_404(Institution,pk=school)
    form = InstitutionRoomsCreateForm()
    if CreateView.method == 'POST':
        data = CreateView.POST
        user_form = InstitutionRoomsCreateForm({
            'institution' : int(school.pk) ,
            'roomtype' : data.get('roomtype') ,
            'therefor' : data.get('therefor') ,
            'rooms' : data.get('rooms') ,
        })
        if user_form.is_valid:
            user_form.save()
            return redirect('building_select',int(school.pk))
        else:
            return render(CreateView,'Buildings/NotValid.html',{'return':'Not Valid'})
    else:
        context = {
            'user_form' : form ,
            'school' : school ,
            'group': group ,
        }
    return render(CreateView,'Buildings/Rooms/Create.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin','SchoolPrincipal'])
def ManageInstitutionBoundryWallCreateView(CreateView,school):
    group = CreateView.user.groups.values('name')
    school = get_object_or_404(Institution,pk=school)
    form = InstitutionBoundaryWallCreateForm()
    if CreateView.method == 'POST':
        data = CreateView.POST
        user_form = InstitutionBoundaryWallCreateForm({
            'institution' : int(school.pk) ,
            'available' : data.get('available') ,
            'ifyes' : data.get('ifyes') ,
        })
        if user_form.is_valid:
            user_form.save()
            return redirect('building_select',int(school.pk))
        else:
            return render(CreateView,'Buildings/NotValid.html',{'return':'Not Valid'})
    else:
        context = {
            'user_form' : form ,
            'school' : school ,
            'group': group ,
        }
    return render(CreateView,'Buildings/BoundaryWall/Create.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin','SchoolPrincipal'])
def ManageInstitutionBuildingConditionCreateView(CreateView,school):
    group = CreateView.user.groups.values('name')
    school = get_object_or_404(Institution,pk=school)
    form = InstitutionBuildingConditionCreateForm()
    if CreateView.method == 'POST':
        data = CreateView.POST
        user_form = InstitutionBuildingConditionCreateForm({
            'institution' : int(school.pk) ,
            'condition' : data.get('condition') ,
            'ifrepairable' : data.get('ifrepairable') ,
        })
        if user_form.is_valid:
            user_form.save()
            return redirect('building_select',int(school.pk))
        else:
            return render(CreateView,'Buildings/NotValid.html',{'return':'Not Valid'})
    else:
        context = {
            'user_form' : form ,
            'school' : school ,
            'group': group ,
        }
    return render(CreateView,'Buildings/BuildingCondition/Create.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin','SchoolPrincipal'])
def ManageInstitutionAreaCreateView(CreateView,school):
    group = CreateView.user.groups.values('name')
    school = get_object_or_404(Institution,pk=school)
    form = InstitutionAreaCreateForm()
    if CreateView.method == 'POST':
        data = CreateView.POST
        user_form = InstitutionAreaCreateForm({
            'institution' : int(school.pk) ,
            'length' : data.get('length') ,
            'width' : data.get('width') ,
        })
        if user_form.is_valid:
            user_form.save()
            return redirect('building_select',int(school.pk))
        else:
            return render(CreateView,'Buildings/NotValid.html',{'return':'Not Valid'})
    else:
        context = {
            'user_form' : form ,
            'school' : school ,
            'group': group ,
        }
    return render(CreateView,'Buildings/Area/Create.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin','SchoolPrincipal'])
def ManageInstitutionWaterAvailabilityCreateView(CreateView,school):
    group = CreateView.user.groups.values('name')
    school = get_object_or_404(Institution,pk=school)
    form = InstitutionWaterAvailiblityCreateForm()
    if CreateView.method == 'POST':
        data = CreateView.POST
        user_form = InstitutionWaterAvailiblityCreateForm({
            'institution' : int(school.pk) ,
            'available' : data.get('available') ,
            'availabletype' : data.get('availabletype') ,
        })
        if user_form.is_valid:
            user_form.save()
            return redirect('building_select',int(school.pk))
        else:
            return render(CreateView,'Buildings/NotValid.html',{'return':'Not Valid'})
    else:
        context = {
            'user_form' : form ,
            'school' : school ,
            'group': group ,
        }
    return render(CreateView,'Buildings/WaterAvailiblity/Create.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin','SchoolPrincipal'])
def ManageInstitutionROPlantAvailabiltyCreateView(CreateView,school):
    group = CreateView.user.groups.values('name')
    school = get_object_or_404(Institution,pk=school)
    form = InstitutionROPlantAvailiblityCreateForm()
    if CreateView.method == 'POST':
        data = CreateView.POST
        user_form = InstitutionROPlantAvailiblityCreateForm({
            'institution' : int(school.pk) ,
            'available' : data.get('available') ,
            'type' : data.get('type') ,
            'qty' : data.get('qty') ,
        })
        if user_form.is_valid:
            user_form.save()
            return redirect('building_select',int(school.pk))
        else:
            return render(CreateView,'Buildings/NotValid.html',{'return':'Not Valid'})
    else:
        context = {
            'user_form' : form ,
            'school' : school ,
            'group': group ,
        }
    return render(CreateView,'Buildings/ROPlantAvailiblity/Create.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin','SchoolPrincipal'])
def ManageInstitutionWaterDispenserAvailabiltyCreateView(CreateView,school):
    group = CreateView.user.groups.values('name')
    school = get_object_or_404(Institution,pk=school)
    form = InstitutionWaterDispenserAvailiblityCreateForm()
    if CreateView.method == 'POST':
        data = CreateView.POST
        user_form = InstitutionWaterDispenserAvailiblityCreateForm({
            'institution' : int(school.pk) ,
            'available' : data.get('available') ,
            'type' : data.get('type') ,
            'qty' : data.get('qty') ,
        })
        if user_form.is_valid:
            user_form.save()
            return redirect('building_select',int(school.pk))
        else:
            return render(CreateView,'Buildings/NotValid.html',{'return':'Not Valid'})
    else:
        context = {
            'user_form' : form ,
            'school' : school ,
            'group': group ,
        }
    return render(CreateView,'Buildings/WaterDispenserAvailiblity/Create.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin','SchoolPrincipal'])
def ManageInstitutionPlayGroundCreateView(CreateView,school):
    group = CreateView.user.groups.values('name')
    school = get_object_or_404(Institution,pk=school)
    form = InstitutionPlayGroundCreateForm()
    if CreateView.method == 'POST':
        data = CreateView.POST
        user_form = InstitutionPlayGroundCreateForm({
            'institution' : int(school.pk) ,
            'available' : data.get('available') ,
            'type' : data.get('type') ,
        })
        if user_form.is_valid:
            user_form.save()
            return redirect('building_select',int(school.pk))
        else:
            return render(CreateView,'Buildings/NotValid.html',{'return':'Not Valid'})
    else:
        context = {
            'user_form' : form ,
            'school' : school ,
            'group': group ,
        }
    return render(CreateView,'Buildings/PlayGround/Create.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin','SchoolPrincipal'])
def ManageInstitutionPlantationCreateView(CreateView,school):
    group = CreateView.user.groups.values('name')
    school = get_object_or_404(Institution,pk=school)
    form = InstitutionPlantationCreateForm()
    if CreateView.method == 'POST':
        data = CreateView.POST
        user_form = InstitutionPlantationCreateForm({
            'institution' : int(school.pk) ,
            'available' : data.get('available') ,
            'qtyoftrees' : data.get('qtyoftrees') ,
            'qtyofplants' : data.get('qtyofplants') ,
        })
        if user_form.is_valid:
            user_form.save()
            return redirect('building_select',int(school.pk))
        else:
            return render(CreateView,'Buildings/NotValid.html',{'return':'Not Valid'})
    else:
        context = {
            'user_form' : form ,
            'school' : school ,
            'group': group ,
        }
    return render(CreateView,'Buildings/Plantation/Create.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin','SchoolPrincipal'])
def ManageInstitutionToiletAvailabiltyCreateView(CreateView,school):
    group = CreateView.user.groups.values('name')
    school = get_object_or_404(Institution,pk=school)
    form = InstitutionToiletAvailiblityCreateForm()
    if CreateView.method == 'POST':
        data = CreateView.POST
        user_form = InstitutionToiletAvailiblityCreateForm({
            'institution' : int(school.pk) ,
            'available' : data.get('available') ,
            'qty' : data.get('qty') ,
            'functionalqty' : data.get('functionalqty') ,
        })
        if user_form.is_valid:
            user_form.save()
            return redirect('building_select',int(school.pk))
        else:
            return render(CreateView,'Buildings/NotValid.html',{'return':'Not Valid'})
    else:
        context = {
            'user_form' : form ,
            'school' : school ,
            'group': group ,
        }
    return render(CreateView,'Buildings/ToiletAvailiblity/Create.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin','SchoolPrincipal'])
def ManageInstitutionWiringAvailabiltyCreateView(CreateView,school):
    group = CreateView.user.groups.values('name')
    school = get_object_or_404(Institution,pk=school)
    form = InstitutionWiringAvailiblityCreateForm()
    if CreateView.method == 'POST':
        data = CreateView.POST
        user_form = InstitutionWiringAvailiblityCreateForm({
            'institution' : int(school.pk) ,
            'available' : data.get('available') ,
            'condition' : data.get('condition') ,
        })
        if user_form.is_valid:
            user_form.save()
            return redirect('building_select',int(school.pk))
        else:
            return render(CreateView,'Buildings/NotValid.html',{'return':'Not Valid'})
    else:
        context = {
            'user_form' : form ,
            'school' : school ,
            'group': group ,
        }
    return render(CreateView,'Buildings/WiringAvailiblity/Create.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin','SchoolPrincipal'])
def ManageInstitutionPlumbingAvailabiltyCreateView(CreateView,school):
    group = CreateView.user.groups.values('name')
    school = get_object_or_404(Institution,pk=school)
    form = InstitutionPlumbingAvailiblityCreateForm()
    if CreateView.method == 'POST':
        data = CreateView.POST
        user_form = InstitutionPlumbingAvailiblityCreateForm({
            'institution' : int(school.pk) ,
            'available' : data.get('available') ,
            'condition' : data.get('condition') ,
        })
        if user_form.is_valid:
            user_form.save()
            return redirect('building_select',int(school.pk))
        else:
            return render(CreateView,'Buildings/NotValid.html',{'return':'Not Valid'})
    else:
        context = {
            'user_form' : form ,
            'school' : school ,
            'group': group ,
        }
    return render(CreateView,'Buildings/PlumbingAvailiblity/Create.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin','SchoolPrincipal'])
def ManageInstitutionSenitaryAvailabiltyCreateView(CreateView,school):
    group = CreateView.user.groups.values('name')
    school = get_object_or_404(Institution,pk=school)
    form = InstitutionSenitaryAvailiblityCreateForm()
    if CreateView.method == 'POST':
        data = CreateView.POST
        user_form = InstitutionSenitaryAvailiblityCreateForm({
            'institution' : int(school.pk) ,
            'available' : data.get('available') ,
        })
        if user_form.is_valid:
            user_form.save()
            return redirect('building_select',int(school.pk))
        else:
            return render(CreateView,'Buildings/NotValid.html',{'return':'Not Valid'})
    else:
        context = {
            'user_form' : form ,
            'school' : school ,
            'group': group ,
        }
    return render(CreateView,'Buildings/SenitaryAvailiblity/Create.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin','SchoolPrincipal'])
def ManageInstitutionElectricityAvailabiltyCreateView(CreateView,school):
    group = CreateView.user.groups.values('name')
    school = get_object_or_404(Institution,pk=school)
    form = InstitutionElectricityAvailiblityCreateForm()
    if CreateView.method == 'POST':
        data = CreateView.POST
        user_form = InstitutionElectricityAvailiblityCreateForm({
            'institution' : int(school.pk) ,
            'available' : data.get('available') ,
            'meter' : data.get('meter') ,
            'meterno' : data.get('meterno') ,
            'consumerno' : data.get('consumerno') ,
            'contactaccnp' : data.get('contactaccnp') ,
            'kunda' : data.get('kunda') ,
            'solar' : data.get('solar') ,
            'solarqty' : data.get('solarqty') ,
        })
        if user_form.is_valid:
            user_form.save()
            return redirect('building_select',int(school.pk))
        else:
            return render(CreateView,'Buildings/NotValid.html',{'return':'Not Valid'})
    else:
        context = {
            'user_form' : form ,
            'school' : school ,
            'group': group ,
        }
    return render(CreateView,'Buildings/ElectricityAvailiblity/Create.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin','SchoolPrincipal'])
def ManageInstitutionFurnitureCreateView(CreateView,school):
    group = CreateView.user.groups.values('name')
    school = get_object_or_404(Institution,pk=school)
    form = InstitutionFurnitureCreateForm()
    if CreateView.method == 'POST':
        data = CreateView.POST
        user_form = InstitutionFurnitureCreateForm({
            'institution' : int(school.pk) ,
            'therefor' : data.get('therefor') ,
            'dualdeskqty' : data.get('dualdeskqty') ,
            'chairsqty' : data.get('chairsqty') ,
            'tablesqty' : data.get('tablesqty') ,
            'shelvesqty' : data.get('shelvesqty') ,
            'lockersqty' : data.get('lockersqty') ,
            'cupboardqty' : data.get('cupboardqty') ,
            'others' : data.get('others') ,
        })
        if user_form.is_valid:
            user_form.save()
            return redirect('building_select',int(school.pk))
        else:
            return render(CreateView,'Buildings/NotValid.html',{'return':'Not Valid'})
    else:
        context = {
            'user_form' : form ,
            'school' : school ,
            'group': group ,
        }
    return render(CreateView,'Buildings/Furniture/Create.html',context)





