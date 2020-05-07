from django.urls import path
from django.conf.urls import url
from . import institutionviews
from . import buildingviews

urlpatterns =[
    path('add/',institutionviews.ManageInstututeCreateView, name = 'institute_create'),
    path('list/',institutionviews.ManageAllInstitutionsListView, name ='institutions_list'),
    path('detail/<school>/admin',institutionviews.ManageAllInstitutionsDetailForAdminView, name ='institution_detail_for_admin'),
    # Building
    path('<school>/building/select',buildingviews.ManageInstitutionBuildingSelectView, name = 'building_select'),
    path('<school>/building/add/select',buildingviews.ManageInstitutionBuildingSelectToAddView, name = 'building_info_add'),

    path('<school>/building/add/room',buildingviews.ManageInstitutionRoomCreateView, name = 'institution_room_create'),
    path('<school>/building/add/boundry_wall',buildingviews.ManageInstitutionBoundryWallCreateView, name = 'institution_boundarywall_create'),
    path('<school>/building/add/building_condition',buildingviews.ManageInstitutionBuildingConditionCreateView, name = 'institution_condition_create'),
    path('<school>/building/add/area',buildingviews.ManageInstitutionAreaCreateView, name = 'institution_area_create'),
    path('<school>/building/add/water_availablity',buildingviews.ManageInstitutionWaterAvailabilityCreateView, name = 'institution_wateravailiblity_create'),
    path('<school>/building/add/roplant_availablity',buildingviews.ManageInstitutionROPlantAvailabiltyCreateView, name = 'institution_roplantavailiblity_create'),
    path('<school>/building/add/water_dispenser',buildingviews.ManageInstitutionWaterDispenserAvailabiltyCreateView, name = 'institution_waterdispenser_create'),
    path('<school>/building/add/playground',buildingviews.ManageInstitutionPlayGroundCreateView, name = 'institution_playground_create'),
    path('<school>/building/add/plantation',buildingviews.ManageInstitutionPlantationCreateView, name = 'institution_plantation_create'),
    path('<school>/building/add/toilet_availability',buildingviews.ManageInstitutionToiletAvailabiltyCreateView, name = 'institution_toiletavailiblity_create'),
    path('<school>/building/add/wiring_availability',buildingviews.ManageInstitutionWiringAvailabiltyCreateView, name = 'institution_wiringavailiblity_create'),
    path('<school>/building/add/plumbing_availability',buildingviews.ManageInstitutionPlumbingAvailabiltyCreateView, name = 'institution_plumbingavailiblity_create'),
    path('<school>/building/add/senitary_availability',buildingviews.ManageInstitutionSenitaryAvailabiltyCreateView, name = 'institution_senitaryavailable_create'),
    path('<school>/building/add/electricity_availability',buildingviews.ManageInstitutionElectricityAvailabiltyCreateView, name = 'institution_electricityavailiblity_create'),
    path('<school>/building/add/furniture',buildingviews.ManageInstitutionFurnitureCreateView, name = 'institution_furniture_create'),


    path('<electricity>/building/electricity',institutionviews.ManageInstitutionElectricityDetailView, name = 'institution_electricity_availiblity'),
    path('<furniture>/building/furniture',institutionviews.ManageInstitutionFurnitureDetailView, name = 'institution_furniture_availiblity'),


]