from django.urls import path
from . import staffviews

urlpatterns = [

    # Staff
    path('staff/add/<school>/<type>',staffviews.ManageInstitutionStaffCreateView, name = 'staff_create'),
    path('profiles/profile/<user>',staffviews.ManageStaffProfileView, name ='staff_profile'),
    path('<school>/staff/select',staffviews.ManageInstitutionStaffTypeSelectView, name ='staff_select'),
    path('profiles/profile/documents/<teacher>',staffviews.ManageStaffDocumentsView, name ='staff_documents'),
    path('profiles/profile/documents/create/<teacher>',staffviews.ManageStaffDocumentsCreateView, name ='staff_documents_create'),
    path('school/profiles/profile/<school>/<type>',staffviews.ManageInstitutionStaffListView, name ='institution_staff_list'),



    path('profiles/principal/<user>',staffviews.ManagePrincipleProfileView, name = 'principal_profile'),
]