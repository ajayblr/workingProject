from django.contrib import admin

from .models import Project
from .models import Defect
from .models import Phase
from .models import Testexecution
from .models import Trend
from .models import Projectstatus
from .models import Testphase
from .models import Notification
from .models import UserProject
# Register your models here.
admin.site.site_header = 'Aj Dashboard'

admin.site.register(Project)
admin.site.register(Defect)
admin.site.register(Phase)
admin.site.register(Testexecution)
admin.site.register(Trend)
admin.site.register(Projectstatus)
admin.site.register(Testphase)
admin.site.register(Notification)
admin.site.register(UserProject)