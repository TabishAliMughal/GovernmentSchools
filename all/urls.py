from django.urls import path
from . import views

urlpatterns = [
    # Main
    path('',views.ManageMainView, name ='main'),
    path('institution/detail/<school>',views.ManageInstitutionDetailForAllView, name ='institution_detail_for_all'),

]