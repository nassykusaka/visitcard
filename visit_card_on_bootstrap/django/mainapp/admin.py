from django.contrib import admin
from .models import Work
from .models import Education
from .models import Hobbies
from .models import Organization


class WorkAdmin(admin.ModelAdmin):
    list_display = ['organization', 'position', 'sdate', 'ldate']


class EducationAdmin(admin.ModelAdmin):
    list_display = ['name', 'specialization']


class OrganizationAdmin(admin.ModelAdmin):
    list_display = ['name', 'area', 'region']

admin.site.register(Work, WorkAdmin)
admin.site.register(Education, EducationAdmin)
admin.site.register(Hobbies)
admin.site.register(Organization, OrganizationAdmin)
