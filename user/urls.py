from django.urls import path
from . import teacherviews

urlpatterns = [

    path('profiles/profile/<user>',teacherviews.ManageTeacherProfileView, name ='teacher_profile'),
    path('profiles/profile/documents/<teacher>',teacherviews.ManageTeacherDocumentsView, name ='teacher_documents'),
]