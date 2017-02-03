from django.contrib import admin

from . import models

admin.site.register(models.Family)
admin.site.register(models.Company)
admin.site.register(models.CompanyInvite)
admin.site.register(models.FamilyInvite)
