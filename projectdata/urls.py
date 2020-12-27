from django.urls import path
from . import views

from django.conf.urls import url
from django.contrib import admin
from .views import home, HomeView, get_data, ChartData, UserView, base

urlpatterns = [
   # path('', views.home, name='projectdata-home'),
    path('', HomeView.as_view(), name='dashboard-home'),
    path('<str:pk>/', HomeView.as_view(), name='dashboard-home'),
    path('projectdata/', UserView.as_view(), name='user-home'),

    path('api/data/', get_data, name='api-data1'),
    path('<str:pk>/api/data/', get_data, name='api-data1'),
    path('api/chart/data/', ChartData.as_view(), name='api-data'),
    path('<str:pk>/api/chart/data/', ChartData.as_view(), name='api-data'),



]
