from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

class Project(models.Model):

    project_name = models.CharField(max_length=30)

    def __str__(self):
        return self.project_name

class Phase(models.Model):

    test_phase = models.CharField(max_length=30, blank=False, null=False)

    def __str__(self):
        return self.test_phase

class Defect(models.Model):
    project_name = models.ForeignKey(Project, on_delete=models.CASCADE)
    project_phase = models.ForeignKey(Phase, on_delete=models.CASCADE)
    new = models.IntegerField()
    assigned_to_fix = models.IntegerField()
    in_progress = models.IntegerField()
    feedback_required = models.IntegerField()
    rfr_in_dev = models.IntegerField()
    passed_in_dev = models.IntegerField()
    rfr_in_test = models.IntegerField()
    passed_in_test = models.IntegerField()
    rfr_in_pre_prod = models.IntegerField()
    additional_fix_required = models.IntegerField()
    ready_for_closure = models.IntegerField()
    closed = models.IntegerField()
    deferred = models.IntegerField()
    rejected = models.IntegerField()
    defect_comments = models.CharField(max_length=30)

    def __str__(self):
        return self.defect_comments

class Testexecution(models.Model):
    project_name = models.ForeignKey(Project, on_delete=models.CASCADE)
    project_phase = models.ForeignKey(Phase, on_delete=models.CASCADE)
    planned_tc = models.IntegerField()
    executed_tc = models.IntegerField()
    passed_tc = models.IntegerField()
    failed_tc = models.IntegerField()
    blocked_tc = models.IntegerField()
    not_applicable_tc = models.IntegerField()
    not_complete_tc = models.IntegerField()
    no_run_tc = models.IntegerField()
    deferred_tc = models.IntegerField()
    text_comments = models.CharField(max_length=30)

    def __str__(self):
        return self.text_comments


class Trend(models.Model):
    project_name = models.ForeignKey(Project, on_delete=models.CASCADE)
    project_phase = models.ForeignKey(Phase, on_delete=models.CASCADE)
    execution_day = models.DateField()
    planned_tc = models.IntegerField()
    passed_tc = models.IntegerField()
    executed_tc = models.IntegerField()
    passed_tc = models.IntegerField()
    failed_tc = models.IntegerField()
    trend_comments = models.CharField(max_length=30)

    def __str__(self):
        return self.trend_comments

class Testphase(models.Model):

    test_phase = models.CharField(max_length=35, blank=False, null=False)

    def __str__(self):
        return self.test_phase

class Projectstatus(models.Model):
    project_name = models.ForeignKey(Project, on_delete=models.CASCADE)
    test_phase = models.ForeignKey(Testphase, on_delete=models.CASCADE)
    completion_status = models.IntegerField()
    text_comments = models.CharField(max_length=29)

    def __str__(self):
        return self.text_comments

class Notification(models.Model):
    project_name = models.ForeignKey(Project, on_delete=models.CASCADE)
    notification_description = models.CharField(max_length=100)
    notification_date = models.DateField()

    def __str__(self):
        return self.notification_description