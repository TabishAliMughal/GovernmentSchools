from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns =[
    path('list/',views.ManageAllInstitutionsListView, name ='institutions_list'),
    path('detail/<school>',views.ManageAllInstitutionsDetailView, name ='institution_detail'),
    path('add/',views.ManageInstututeCreateView, name = 'institute_create'),
    path('<school>/staff/select',views.ManageInstitutionStaffTypeSelectView, name ='staff_select'),
    path('school/profiles/profile/<school>/<type>',views.ManageSchoolStaffListView, name ='school_teacher_list'),


]