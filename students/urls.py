from django.urls import path
from . import views

urlpatterns = [
    path('<school>/list/',views.ManageStudentListView, name = 'student_list'),
    path('<school>/add/',views.ManageStudentCreateView, name = 'student_create'),
    path('<school>/detail/<gr>', views.ManageStudentDetailView, name = 'student_detail'),
    path('<school>/delete/<gr>', views.ManageStudentDeleteView, name = 'student_delete'),
    path('<school>/edit/<gr>', views.ManageStudentEditView, name = 'student_edit'),
    path('<school>/upload', views.student_upload, name = 'student_upload'),
    path('download', views.student_download, name = 'student_download'),


   

]