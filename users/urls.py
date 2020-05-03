from django.urls import path
from . import views
from . import adminviews
from . import teacherviews

urlpatterns = [
    # Main
    path('',views.ManageMainView, name ='main'),


    path('profiles/',adminviews.ManageAllProfilesView, name ='profiles'),


    path('profiles/profile',teacherviews.ManageTeacherProfileView, name ='teacher_profile'),
]