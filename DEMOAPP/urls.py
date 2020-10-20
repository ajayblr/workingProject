from django.urls import path
from . import views

urlpatterns = [
    path('', views.hi,  name='home-page'),
    path('', views.about,  name='about-page'),
    path('', views.smallchanges,  name='small-changes')
]
