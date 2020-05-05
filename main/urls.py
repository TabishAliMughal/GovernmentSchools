from django.urls import path
from . import views

urlpatterns = [
    # Main
    path('',views.ManageMainView, name ='main'),

]