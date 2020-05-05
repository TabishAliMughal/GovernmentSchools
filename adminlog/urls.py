from django.urls import path
from . import adminviews

urlpatterns = [

    path('profiles/',adminviews.ManageAllProfilesView, name ='profiles'),


]