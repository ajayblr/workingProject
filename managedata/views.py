from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.views.generic import TemplateView

from projectdata.models import Defect, Projectstatus, Trend, Testexecution

from django_globals import globals
from django.template import loader

from datetime import date

from django.views.generic import View
from .forms import DefectForm, PreperationStatusForm, TrendForm, ProgressForm

def index(request):

    obj = Defect.objects.all().order_by('project_name')
    statusobj = Projectstatus.objects.all().order_by('project_name')
    trendobj = Trend.objects.all().order_by('project_name','execution_day')
    progressobj = Testexecution.objects.all()



    template = loader.get_template('managedata/index.html')

    context = {
       'obj': obj,
       'statusobj': statusobj,
       'trendobj': trendobj,
       'progressobj': progressobj
    }
    return HttpResponse(template.render(context, request))

def createDefect(request):
        form = DefectForm()

        if request.method == 'POST':
            form = DefectForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/managedata')

        context = {'form':form}
        return render(request, 'managedata/defect_form.html', context)

def updateDefect(request, pk):
    defect = Defect.objects.get(id=pk)
    form = DefectForm(instance=defect)

    if request.method == 'POST':
        form = DefectForm(request.POST, instance=defect)
        if form.is_valid():
            form.save()
            return redirect('/managedata')

    context = {'form': form}
    return render(request, 'managedata/defect_form.html', context)

def deleteDefect(request, pk):
    defect = Defect.objects.get(id=pk)
    if request.method == 'POST':
        defect.delete()
        return redirect('/managedata')

    context = {'defect':defect}
    return render(request, 'managedata/deletedefect.html', context)

def createStatus(request):
    form = PreperationStatusForm()

    if request.method == 'POST':
        form = PreperationStatusForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/managedata')

    context = {'form': form}
    return render(request, 'managedata/status_form.html', context)

def updateStatus(request, pk):
    status = Projectstatus.objects.get(id=pk)
    form = PreperationStatusForm(instance=status)

    if request.method == 'POST':
        form = PreperationStatusForm(request.POST, instance=status)
        if form.is_valid():
            form.save()
            return redirect('/managedata')

    context = {'form': form}
    return render(request, 'managedata/status_form.html', context)

def deleteStatus(request, pk):
    status = Projectstatus.objects.get(id=pk)
    if request.method == 'POST':
        status.delete()
        return redirect('/managedata')

    context = {'status':status}
    return render(request, 'managedata/deletestatus.html', context)

def createTrend(request):
        form = TrendForm()

        if request.method == 'POST':
            form = TrendForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/managedata')

        context = {'form': form}
        return render(request, 'managedata/trend_form.html', context)

def updateTrend(request, pk):
        trend = Trend.objects.get(id=pk)
        form = TrendForm(instance=trend)

        if request.method == 'POST':
            form = TrendForm(request.POST, instance=trend)
            if form.is_valid():
                form.save()
                return redirect('/managedata')

        context = {'form': form}
        return render(request, 'managedata/trend_form.html', context)

def deleteTrend(request, pk):
    trend = Trend.objects.get(id=pk)
    if request.method == 'POST':
        trend.delete()
        return redirect('/managedata')

    context = {'trend':trend}
    return render(request, 'managedata/deletetrend.html', context)

def createProgress(request):
        form = ProgressForm()

        if request.method == 'POST':
            form = ProgressForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/managedata')

        context = {'form': form}
        return render(request, 'managedata/progress_form.html', context)


def updateProgress(request, pk):
    progress = Testexecution.objects.get(id=pk)
    form = ProgressForm(instance=progress)

    if request.method == 'POST':
        form = ProgressForm(request.POST, instance=progress)
        if form.is_valid():
            form.save()
            return redirect('/managedata')

    context = {'form': form}
    return render(request, 'managedata/progress_form.html', context)


def deleteProgress(request, pk):
    progress = Testexecution.objects.get(id=pk)
    if request.method == 'POST':
        progress.delete()
        return redirect('/managedata')

    context = {'progress': progress}
    return render(request, 'managedata/deleteprogress.html', context)