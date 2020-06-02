from django.urls import path
from . import views

urlpatterns = [
    path('news/<school>',views.ManageNewsListView, name = 'news_list'),
    path('news/<school>/add', views.ManageNewsCreateView, name = 'institution_news_create'),
    path('news/<school>/delete/<news_code>', views.ManageNewsDeleteView, name = 'institution_news_delete'),
    path('activity/<school>/add', views.ManageActivityCreateView, name = 'institution_activity_create'),
    path('activity/<school>/delete/<activity_code>', views.ManageActivityDeleteView, name = 'institution_activity_delete'),

]