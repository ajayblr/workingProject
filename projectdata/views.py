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
from .models import UserProject
from .models import Testexecution
from django_globals import globals
from django.template.loader import render_to_string

from datetime import date

from django.views.generic import View
from rest_framework.views import APIView
from rest_framework.response import Response

User = get_user_model()

pjcode = 1

def home(request):
    context = {
        'projectdefect': Defect.objects.all()
    }
    return render(request,'projectdata/index.html', context)


class HomeView(View):
    #def get(self, request, *args, **kwargs):

    def get(self, request, pk):
        global pjcode, GLOBAL_Entry
        print("Project Name =", pk)
        myProjects = Project.objects.all().filter(project_name=pk)
        pjcode=myProjects[0].id
        print("Project code =", pjcode)
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
    global pjcode
    tdaysnotif = Notification.objects.all().filter(notification_date=date.today())
    myProjects = Project.objects.all()
    stobj = Projectstatus.objects.all().filter(project_name=pjcode).filter(test_phase=1)
    sitobj = Projectstatus.objects.all().filter(project_name=pjcode).filter(test_phase=2)
    uatobj = Projectstatus.objects.all().filter(project_name=pjcode).filter(test_phase=3)
    myProjAccess = UserProject.objects.all().filter(user_name = request.user.id)

    projaccess = []
    for i in range(0, len(myProjAccess)):
        l = myProjAccess[i].project_name
        projaccess.append(l)
        #print(l)

    projaccesscode = []
    for i in range(0, len(myProjAccess)):
        l = myProjAccess[i].id
        projaccesscode.append(l)
        #print(l)

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

    return {'notifylist': notifylist, 'len_ntf':len(notifylist), 'stpercentage': stpercentage, 'sitpercentage': sitpercentage, 'uatpercentage': uatpercentage, 'projlist':projlist, 'projaccess':projaccess, 'projacesscode':projaccesscode}

class ChartData(APIView):
    global pjcode
    authentication_classes = []
    permission_classes = []


    def get(self, request, format=None):

        # Get the data for all the graphs from the data model

        # Get the defect data for the graphs from the data model
        stdefects = Defect.objects.all().filter(project_name=pjcode).filter(project_phase=2)
        sitdefects = Defect.objects.all().filter(project_name=pjcode).filter(project_phase=3)
        uatdefects = Defect.objects.all().filter(project_name=pjcode).filter(project_phase=4)

        stprepstatus = Projectstatus.objects.all().filter(project_name=pjcode).filter(test_phase=1)
        sitprepstatus = Projectstatus.objects.all().filter(project_name=pjcode).filter(test_phase=2)
        uatprepstatus = Projectstatus.objects.all().filter(project_name=pjcode).filter(test_phase=3)

        stexecstatus = Projectstatus.objects.all().filter(project_name=pjcode).filter(test_phase=4)
        sitexecstatus = Projectstatus.objects.all().filter(project_name=pjcode).filter(test_phase=5)
        uatexecstatus = Projectstatus.objects.all().filter(project_name=pjcode).filter(test_phase=6)

        stexecprogress= Testexecution.objects.all().filter(project_name=pjcode).filter(project_phase=2)
        sitexecprogress = Testexecution.objects.all().filter(project_name=pjcode).filter(project_phase=3)
        uatexecprogress = Testexecution.objects.all().filter(project_name=pjcode).filter(project_phase=4)

        progresslabel = ["Planned", "Executed", "Passed", "Failed", "Blocked", "N/A", "Not Completed", "No run", "Deferred"]

        stexectrendstatus = Trend.objects.all().filter(project_name=pjcode).filter(project_phase=2).order_by('execution_day')

        # Get the defect labels
        defectlabels = ["New", "Assigned to Fix", "In Progress",
                  "Feedback Required", "R4R in Dev", "Passed in Dev",
                  "R4R in Test", "Passed in test", "R4R in Pre-Prod",
                  "Additional Fix Required", "Ready for Closure",
                  "Closed", "Deferred", "Rejected"
                  ]
        # get defect status related to the project
        stdefectitems = [stdefects[0].new, stdefects[0].assigned_to_fix, stdefects[0].in_progress,
                         stdefects[0].feedback_required, stdefects[0].rfr_in_dev, stdefects[0].passed_in_dev,
                         stdefects[0].rfr_in_test, stdefects[0].passed_in_test, stdefects[0].rfr_in_pre_prod,
                         stdefects[0].additional_fix_required, stdefects[0].ready_for_closure, stdefects[0].closed,
                         stdefects[0].deferred, stdefects[0].rejected]

        # get defect status related to the project
        sitdefectitems = [sitdefects[0].new, sitdefects[0].assigned_to_fix, sitdefects[0].in_progress,
                          sitdefects[0].feedback_required, sitdefects[0].rfr_in_dev, sitdefects[0].passed_in_dev,
                          sitdefects[0].rfr_in_test, sitdefects[0].passed_in_test, sitdefects[0].rfr_in_pre_prod,
                          sitdefects[0].additional_fix_required, sitdefects[0].ready_for_closure, sitdefects[0].closed,
                          sitdefects[0].deferred, sitdefects[0].rejected]

        # get defect status related to the project
        uatdefectitems = [uatdefects[0].new, uatdefects[0].assigned_to_fix, uatdefects[0].in_progress,
                          uatdefects[0].feedback_required, uatdefects[0].rfr_in_dev, uatdefects[0].passed_in_dev,
                          uatdefects[0].rfr_in_test, uatdefects[0].passed_in_test, uatdefects[0].rfr_in_pre_prod,
                          uatdefects[0].additional_fix_required, uatdefects[0].ready_for_closure, uatdefects[0].closed,
                          uatdefects[0].deferred, uatdefects[0].rejected]

        # get the Test phase preparation status for the selected project
        stprepitem = [stprepstatus[0].completion_status, 100-stprepstatus[0].completion_status]
        sitprepitem = [sitprepstatus[0].completion_status, 100 - sitprepstatus[0].completion_status]
        uatprepitem = [uatprepstatus[0].completion_status, 100 - uatprepstatus[0].completion_status]

        # get the Test phase Execution status for the selected project
        stexecitem = [stexecstatus[0].completion_status, 100 - stexecstatus[0].completion_status]
        sitexecitem = [sitexecstatus[0].completion_status, 100 - sitexecstatus[0].completion_status]
        uatexecitem = [uatexecstatus[0].completion_status, 100 - uatexecstatus[0].completion_status]

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
            "stdefectitems": stdefectitems,
            "sitdefectitems": sitdefectitems,
            "uatdefectitems": uatdefectitems,
            "stprepitems": stprepitem,
            "sitprepitems": sitprepitem,
            "uatprepitems": uatprepitem,
            "stexecitems": stexecitem,
            "sitexecitems": sitexecitem,
            "uatexecitems": uatexecitem,
            "sttrenditems": sttrenditem,
            "sttrenddatelabel": sttrenddate,
            "progresslabels": progresslabel

            #"default": mydefects,
        }

        return Response(data )


class UserView(View):
        def get(self, request, *args, **kwargs):
            return render(request, 'projectdata/user.html', {} )

