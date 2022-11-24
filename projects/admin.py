from django.contrib import admin
from .models import ProjectModel,ProjectTask,ProjectInvite
# Register your models here.


admin.site.register(ProjectModel)
admin.site.register(ProjectTask)
admin.site.register(ProjectInvite)