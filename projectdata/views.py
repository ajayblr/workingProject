from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.views.generic import TemplateView

from django.http import JsonResponse
from .models import Defect
from .models import Projectstatus
from .models import Trend
from .models import Notification
from .models import Project

from django.template.loader import render_to_string

from datetime import date

from django.views.generic import View
from rest_framework.views import APIView
from rest_framework.response import Response

User = get_user_model()

def home(request):
    context = {
        'projectdefect': Defect.objects.all()
    }
    return render(request,'projectdata/index.html', context)


class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'projectdata/dashboard.html', {})

def get_data(request, *args, **kwargs):
    tdaysnotif = Notification.objects.all()

    notifylist = []
    for i in range(0, len(tdaysnotif)):
        l = tdaysnotif[i].notification_description
        notifylist.append(l)

    data = {
        "notifydata": notifylist
    }
    return JsonResponse(data)

def base(request):
    tdaysnotif = Notification.objects.all().filter(notification_date=date.today())
    myProjects = Project.objects.all()
    stobj = Projectstatus.objects.all().filter(project_name=1).filter(test_phase=1)
    sitobj = Projectstatus.objects.all().filter(project_name=1).filter(test_phase=2)
    uatobj = Projectstatus.objects.all().filter(project_name=1).filter(test_phase=3)

    projlist = []
    for i in range(0, len(myProjects)):
        l = myProjects[i].project_name
        projlist.append(l)

    stpercentage = stobj[0].completion_status
    sitpercentage = sitobj[0].completion_status
    uatpercentage = uatobj[0].completion_status

    notifylist = []
    for i in range(0, len(tdaysnotif)):
        l = tdaysnotif[i].notification_description
        notifylist.append(l)

    return {'notifylist': notifylist, 'len_ntf':len(notifylist), 'stpercentage': stpercentage, 'sitpercentage': sitpercentage, 'uatpercentage': uatpercentage, 'projlist':projlist}

class ChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        defects = Defect.objects.all().filter(project_name=1)
        stprepstatus = Projectstatus.objects.all().filter(project_name=1).filter(test_phase=1)
        sitprepstatus = Projectstatus.objects.all().filter(project_name=1).filter(test_phase=2)
        uatprepstatus = Projectstatus.objects.all().filter(project_name=1).filter(test_phase=3)
        stexectrendstatus = Trend.objects.all().filter(project_name=1).filter(project_phase=2).order_by('execution_day')

        defectlabels = ["New", "Assigned to Fix", "In Progress",
                  "Feedback Required", "R4R in Dev", "Passed in Dev",
                  "R4R in Test", "Passed in test", "R4R in Pre-Prod",
                  "Additional Fix Required", "Ready for Closure",
                  "Closed", "Deferred", "Rejected"
                  ]
        # get defect status related to the project
        defectitems = [defects[0].new, defects[0].assigned_to_fix, defects[0].in_progress,
                         defects[0].feedback_required, defects[0].rfr_in_dev, defects[0].passed_in_dev,
                         defects[0].rfr_in_test, defects[0].passed_in_test, defects[0].rfr_in_pre_prod,
                         defects[0].additional_fix_required, defects[0].ready_for_closure, defects[0].closed,
                         defects[0].deferred, defects[0].rejected]


        # get the Test phase preparation status
        stprepitem = [stprepstatus[0].completion_status, 100-stprepstatus[0].completion_status]
        sitprepitem = [sitprepstatus[0].completion_status, 100 - sitprepstatus[0].completion_status]
        uatprepitem = [uatprepstatus[0].completion_status, 100 - uatprepstatus[0].completion_status]

        sttrenditem = []
        sttrenddate = []
        pltc = []
        extc = []
        patc = []
        fatc = []
        for i in range(0, len(stexectrendstatus)):
            x = stexectrendstatus[i].planned_tc
            y = stexectrendstatus[i].executed_tc
            z = stexectrendstatus[i].passed_tc
            a = stexectrendstatus[i].failed_tc
            b = stexectrendstatus[i].execution_day.strftime('%d %b')
            sttrenddate.append(b)
            pltc.append(x)
            extc.append(y)
            patc.append(z)
            fatc.append(a)
        sttrenditem.append(pltc)
        sttrenditem.append(extc)
        sttrenditem.append(patc)
        sttrenditem.append(fatc)

        data = {
            "defectlabels":  defectlabels,
            "defectitems": defectitems,
            "stprepitems": stprepitem,
            "sitprepitems": sitprepitem,
            "uatprepitems": uatprepitem,
            "sttrenditems": sttrenditem,
            "sttrenddatelabel": sttrenddate,

            #"default": mydefects,
        }

        return Response(data )


class UserView(View):
        def get(self, request, *args, **kwargs):
            return render(request, 'projectdata/user.html', {} )


