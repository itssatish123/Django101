from django.contrib import admin
from ourServiceDetail.models import ourService
# Register your models here.
class serviceAdmin(admin.ModelAdmin):
    list = ('servicesTitle','serviceDesc','Descritionval','Our_image')

admin.site.register(ourService,serviceAdmin)