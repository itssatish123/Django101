from django.contrib import admin
from .models import rechargePlans
# Register your models here.
class planAdmin(admin.ModelAdmin):
    list_display = ('planName', 'planPrice', 'planValidity', 'planStar', 'planData', 'ValidityDescription', 'planApi')  

admin.site.register(rechargePlans, planAdmin)