from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.views.generic import TemplateView


def hi(request):
    return render(request, 'DEMOAPP/hi.html',{'title': 'Ajs Dashboard'})

def smallchanges(request):
    return render(request, 'DEMOAPP/smallchanges.html',{'title': 'Small Changes - Q2-2020'})

def about(request):
    return render(request, 'DEMOAPP/about.html', {'title': 'About my Page'})

