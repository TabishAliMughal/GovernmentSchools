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
    path('<staff>/<institution>/staff/delete',staffviews.ManageInstitutionStaffDeleteView, name = 'staff_delete'),
    path('<staff>/<institution>/staff/edit',staffviews.ManageInstitutionStaffEditView, name = 'staff_edit'),
    path('staff/<school>/upload/<type>',staffviews.staff_upload, name = 'staff_upload'),
    path('staff/download',staffviews.staff_download, name = 'staff_download'),
    path('staff/detail/<school>/<employ>',staffviews.ManageInstitutionStaffDetailView, name = 'staff_detail'),







    path('profiles/principal/<user>',staffviews.ManagePrincipleProfileView, name = 'principal_profile'),
]