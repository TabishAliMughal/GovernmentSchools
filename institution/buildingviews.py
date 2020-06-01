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
            return redirect('institution_room_list', int(school.pk))
        else:
            return render(CreateView,'Buildings/NotValid.html',{'return':'Not Valid'})
    else:
        context = {
            'user_form' : form ,
            'school' : school ,
            'group': group ,
        }
    return render(CreateView,'Buildings/Rooms/Create.html',context)

def ManageRoomListView(ListView,school):
    group = ListView.user.groups.values('name')
    school = get_object_or_404(Institution , pk = int(school))
    rooms = []
    for i in InstitutionRooms.objects.all():
        if str(i.institution.pk) == str(school.pk):
            rooms.append(i)
    context = {
        'school': school ,
        'rooms': rooms,
        'group': group ,
    }
    return render(ListView,'Buildings/Rooms/List.html',context)

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
            return redirect('institution_boundrywall_list',int(school.pk))
        else:
            return render(CreateView,'Buildings/NotValid.html',{'return':'Not Valid'})
    else:
        context = {
            'user_form' : form ,
            'school' : school ,
            'group': group ,
        }
    return render(CreateView,'Buildings/BoundaryWall/Create.html',context)

def ManageBoundryWallListView(ListView,school):
    group = ListView.user.groups.values('name')
    school = get_object_or_404(Institution , pk = int(school))
    boundrywall = []
    for i in InstitutionBoundaryWall.objects.all():
        if str(i.institution.pk) == str(school.pk):
            boundrywall.append(i)
    context = {
        'school': school ,
        'boundrywall': boundrywall,
        'group': group ,
    }
    return render(ListView,'Buildings/BoundaryWall/List.html',context)

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
            return redirect('institution_condition_list',int(school.pk))
        else:
            return render(CreateView,'Buildings/NotValid.html',{'return':'Not Valid'})
    else:
        context = {
            'user_form' : form ,
            'school' : school ,
            'group': group ,
        }
    return render(CreateView,'Buildings/BuildingCondition/Create.html',context)


def ManageConditionListView(ListView,school):
    group = ListView.user.groups.values('name')
    school = get_object_or_404(Institution , pk = int(school))
    condition = []
    for i in InstitutionBuildingCondition.objects.all():
        if str(i.institution.pk) == str(school.pk):
            condition.append(i)
    context = {
        'school': school ,
        'condition': condition,
        'group': group ,
    }
    return render(ListView,'Buildings/BuildingCondition/List.html',context)

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
            return redirect('institution_area_list',int(school.pk))
        else:
            return render(CreateView,'Buildings/NotValid.html',{'return':'Not Valid'})
    else:
        context = {
            'user_form' : form ,
            'school' : school ,
            'group': group ,
        }
    return render(CreateView,'Buildings/Area/Create.html',context)

def ManageAreaListView(ListView,school):
    group = ListView.user.groups.values('name')
    school = get_object_or_404(Institution , pk = int(school))
    area = []
    for i in InstitutionArea.objects.all():
        if str(i.institution.pk) == str(school.pk):
            area.append(i)
    context = {
        'school': school ,
        'area': area,
        'group': group ,
    }
    return render(ListView,'Buildings/Area/List.html',context)

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
            return redirect('institution_water_availability_list',int(school.pk))
        else:
            return render(CreateView,'Buildings/NotValid.html',{'return':'Not Valid'})
    else:
        context = {
            'user_form' : form ,
            'school' : school ,
            'group': group ,
        }
    return render(CreateView,'Buildings/WaterAvailiblity/Create.html',context)

def ManageWaterAvailabilityListView(ListView,school):
    group = ListView.user.groups.values('name')
    school = get_object_or_404(Institution , pk = int(school))
    water = []
    for i in InstitutionWaterAvailiblity.objects.all():
        if str(i.institution.pk) == str(school.pk):
            water.append(i)
    context = {
        'school': school ,
        'water': water,
        'group': group ,
    }
    return render(ListView,'Buildings/WaterAvailiblity/List.html',context)

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
            return redirect('institution_ROPlant_availability_list',int(school.pk))
        else:
            return render(CreateView,'Buildings/NotValid.html',{'return':'Not Valid'})
    else:
        context = {
            'user_form' : form ,
            'school' : school ,
            'group': group ,
        }
    return render(CreateView,'Buildings/ROPlantAvailiblity/Create.html',context)

def ManageROPlantAvailabilityListView(ListView,school):
    group = ListView.user.groups.values('name')
    school = get_object_or_404(Institution , pk = int(school))
    ro = []
    for i in InstitutionROPlantAvailiblity.objects.all():
        if str(i.institution.pk) == str(school.pk):
            ro.append(i)
    context = {
        'school': school ,
        'ro': ro,
        'group': group ,
    }
    return render(ListView,'Buildings/ROPlantAvailiblity/List.html',context)

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
            return redirect('institution_dispenser_availability_list',int(school.pk))
        else:
            return render(CreateView,'Buildings/NotValid.html',{'return':'Not Valid'})
    else:
        context = {
            'user_form' : form ,
            'school' : school ,
            'group': group ,
        }
    return render(CreateView,'Buildings/WaterDispenserAvailiblity/Create.html',context)

def ManageDispenserAvailabilityListView(ListView,school):
    group = ListView.user.groups.values('name')
    school = get_object_or_404(Institution , pk = int(school))
    dispenser = []
    for i in InstitutionWaterDispenserAvailiblity.objects.all():
        if str(i.institution.pk) == str(school.pk):
            dispenser.append(i)
    context = {
        'school': school ,
        'dispenser': dispenser,
        'group': group ,
    }
    return render(ListView,'Buildings/WaterDispenserAvailiblity/List.html',context)

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
            return redirect('institution_playground_list',int(school.pk))
        else:
            return render(CreateView,'Buildings/NotValid.html',{'return':'Not Valid'})
    else:
        context = {
            'user_form' : form ,
            'school' : school ,
            'group': group ,
        }
    return render(CreateView,'Buildings/PlayGround/Create.html',context)


def ManagePlaygroundListView(ListView,school):
    group = ListView.user.groups.values('name')
    school = get_object_or_404(Institution , pk = int(school))
    playground = []
    for i in InstitutionPlayGround.objects.all():
        if str(i.institution.pk) == str(school.pk):
            playground.append(i)
    context = {
        'school': school ,
        'playground': playground,
        'group': group ,
    }
    return render(ListView,'Buildings/PlayGround/List.html',context)

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
            return redirect('institution_plantation_list',int(school.pk))
        else:
            return render(CreateView,'Buildings/NotValid.html',{'return':'Not Valid'})
    else:
        context = {
            'user_form' : form ,
            'school' : school ,
            'group': group ,
        }
    return render(CreateView,'Buildings/Plantation/Create.html',context)

def ManagePlantationListView(ListView,school):
    group = ListView.user.groups.values('name')
    school = get_object_or_404(Institution , pk = int(school))
    plantation = []
    for i in InstitutionPlantation.objects.all():
        if str(i.institution.pk) == str(school.pk):
            plantation.append(i)
    context = {
        'school': school ,
        'plantation': plantation,
        'group': group ,
    }
    return render(ListView,'Buildings/Plantation/List.html',context)

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
            return redirect('institution_toilet_list',int(school.pk))
        else:
            return render(CreateView,'Buildings/NotValid.html',{'return':'Not Valid'})
    else:
        context = {
            'user_form' : form ,
            'school' : school ,
            'group': group ,
        }
    return render(CreateView,'Buildings/ToiletAvailiblity/Create.html',context)

def ManageToiletListView(ListView,school):
    group = ListView.user.groups.values('name')
    school = get_object_or_404(Institution , pk = int(school))
    toilet = []
    for i in InstitutionToiletAvailiblity.objects.all():
        if str(i.institution.pk) == str(school.pk):
            toilet.append(i)
    context = {
        'school': school ,
        'toilet': toilet,
        'group': group ,
    }
    return render(ListView,'Buildings/ToiletAvailiblity/List.html',context)

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
            return redirect('institution_wiring_list',int(school.pk))
        else:
            return render(CreateView,'Buildings/NotValid.html',{'return':'Not Valid'})
    else:
        context = {
            'user_form' : form ,
            'school' : school ,
            'group': group ,
        }
    return render(CreateView,'Buildings/WiringAvailiblity/Create.html',context)

def ManageWiringListView(ListView,school):
    group = ListView.user.groups.values('name')
    school = get_object_or_404(Institution , pk = int(school))
    wiring = []
    for i in InstitutionWiringAvailiblity.objects.all():
        if str(i.institution.pk) == str(school.pk):
            wiring.append(i)
    context = {
        'school': school ,
        'wiring': wiring,
        'group': group ,
    }
    return render(ListView,'Buildings/WiringAvailiblity/List.html',context)

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
            return redirect('institution_plumbing_list',int(school.pk))
        else:
            return render(CreateView,'Buildings/NotValid.html',{'return':'Not Valid'})
    else:
        context = {
            'user_form' : form ,
            'school' : school ,
            'group': group ,
        }
    return render(CreateView,'Buildings/PlumbingAvailiblity/Create.html',context)

def ManagePlumbingListView(ListView,school):
    group = ListView.user.groups.values('name')
    school = get_object_or_404(Institution , pk = int(school))
    plumbing = []
    for i in InstitutionPlumbingAvailiblity.objects.all():
        if str(i.institution.pk) == str(school.pk):
            plumbing.append(i)
    context = {
        'school': school ,
        'plumbing': plumbing,
        'group': group ,
    }
    return render(ListView,'Buildings/PlumbingAvailiblity/List.html',context)

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
            return redirect('institution_senitary_list',int(school.pk))
        else:
            return render(CreateView,'Buildings/NotValid.html',{'return':'Not Valid'})
    else:
        context = {
            'user_form' : form ,
            'school' : school ,
            'group': group ,
        }
    return render(CreateView,'Buildings/SenitaryAvailiblity/Create.html',context)

def ManageSenitaryListView(ListView,school):
    group = ListView.user.groups.values('name')
    school = get_object_or_404(Institution , pk = int(school))
    senitary = []
    for i in InstitutionSenitaryAvailiblity.objects.all():
        if str(i.institution.pk) == str(school.pk):
            senitary.append(i)
    context = {
        'school': school ,
        'senitary': senitary,
        'group': group ,
    }
    return render(ListView,'Buildings/SenitaryAvailiblity/List.html',context)

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
            return redirect('institution_electricity_list',int(school.pk))
        else:
            return render(CreateView,'Buildings/NotValid.html',{'return':'Not Valid'})
    else:
        context = {
            'user_form' : form ,
            'school' : school ,
            'group': group ,
        }
    return render(CreateView,'Buildings/ElectricityAvailiblity/Create.html',context)

def ManageElectricityListView(ListView,school):
    group = ListView.user.groups.values('name')
    school = get_object_or_404(Institution , pk = int(school))
    electricity = []
    for i in InstitutionElectricityAvailiblity.objects.all():
        if str(i.institution.pk) == str(school.pk):
            electricity.append(i)
    context = {
        'school': school ,
        'electricity': electricity,
        'group': group ,
    }
    return render(ListView,'Buildings/ElectricityAvailiblity/List.html',context)

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
            return redirect('institution_furniture_list',int(school.pk))
        else:
            return render(CreateView,'Buildings/NotValid.html',{'return':'Not Valid'})
    else:
        context = {
            'user_form' : form ,
            'school' : school ,
            'group': group ,
        }
    return render(CreateView,'Buildings/Furniture/Create.html',context)

def ManageFurnitureListView(ListView,school):
    group = ListView.user.groups.values('name')
    school = get_object_or_404(Institution , pk = int(school))
    furniture = []
    for i in InstitutionFurniture.objects.all():
        if str(i.institution.pk) == str(school.pk):
            furniture.append(i)
    context = {
        'school': school ,
        'furniture': furniture,
        'group': group ,
    }
    return render(ListView,'Buildings/Furniture/List.html',context)





