from django.urls import path
from . import listviews
from . import createviews

urlpatterns = [
    # List
    path('provence/list/',listviews.ManageProvenceListView, name = 'provence_list'),
    path('division/list/',listviews.ManageDivisionListView, name = 'division_list'),
    path('district/list/',listviews.ManageDistrictListView, name = 'district_list'),
    path('tehsil/list/',listviews.ManageTehsilListView, name = 'tehsil_list'),
    path('unioncouncil/list/',listviews.ManageUnionCouncilListView, name = 'unioncouncil_list'),
    path('qualification/list/',listviews.ManageQualificationListView, name = 'qualification_list'),
    path('documenttype/list/',listviews.ManageDocumentTypeListView, name = 'documenttype_list'),
    path('stafftype/list/',listviews.ManageStaffTypeListView, name = 'stafftype_list'),
    path('roomtype/list/',listviews.ManageRoomTypeListView, name = 'roomtype_list'),

    # Create
    path('provence/create/',createviews.ManageProvenceCreateView, name = 'provence_create'),
    path('division/create/',createviews.ManageDivisionCreateView, name = 'division_create'),
    path('district/create/',createviews.ManageDistrictCreateView, name = 'district_create'),
    path('tehsil/create/',createviews.ManageTehsilCreateView, name = 'tehsil_create'),
    path('unioncouncil/create/',createviews.ManageUnionCouncilCreateView, name = 'unioncouncil_create'),
    path('qualification/create/',createviews.ManageQualificationCreateView, name = 'qualification_create'),
    path('documenttype/create/',createviews.ManageDocumentTypeCreateView, name = 'documenttype_create'),
    path('stafftype/create/',createviews.ManageStaffTypeCreateView, name = 'stafftype_create'),
    path('roomtype/create/',createviews.ManageRoomTypeCreateView, name = 'roomtype_create'),
]