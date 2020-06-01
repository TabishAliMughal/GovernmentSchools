from django.urls import path
from . import views

urlpatterns = [
    path('news/<school>',views.ManageNewsListView, name = 'news_list'),

]