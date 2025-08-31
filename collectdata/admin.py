from django.contrib import admin
from collectdata.models import collectFormData

# Register your models here.
class collectDataAdmin(admin.ModelAdmin):
    list = ('userName','userEmail','userMess')

admin.site.register(collectFormData,collectDataAdmin)