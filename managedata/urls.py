from django.conf.urls import url
from django.urls import path
from . import views


urlpatterns = [
    url('^$', views.index, name='index'),
    path('create_defect/', views.createDefect, name="create_defect"),
    path('update_defect/<str:pk>', views.updateDefect, name="update_defect"),
    path('delete_defect/<str:pk>', views.deleteDefect, name="delete_defect"),

    path('create_status/', views.createStatus, name="create_status"),
    path('update_status/<str:pk>', views.updateStatus, name="update_status"),
    path('delete_status/<str:pk>', views.deleteStatus, name="delete_status"),

    path('create_trend/', views.createTrend, name="create_trend"),
    path('update_trend/<str:pk>', views.updateTrend, name="update_trend"),
    path('delete_trend/<str:pk>', views.deleteTrend, name="delete_trend"),

    path('create_progress/', views.createProgress, name="create_progress"),
    path('update_progress/<str:pk>', views.updateProgress, name="update_progress"),
    path('delete_progress/<str:pk>', views.deleteProgress, name="delete_progress"),
]
