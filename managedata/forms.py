from django.forms import ModelForm
from projectdata.models import Defect, Projectstatus, Trend, Testexecution

class DefectForm(ModelForm):
    class Meta:
        model = Defect
        fields = '__all__'

class PreperationStatusForm(ModelForm):
    class Meta:
        model = Projectstatus
        fields = '__all__'


class TrendForm(ModelForm):
    class Meta:
        model = Trend
        fields = '__all__'


class ProgressForm(ModelForm):
    class Meta:
        model = Testexecution
        fields = '__all__'
