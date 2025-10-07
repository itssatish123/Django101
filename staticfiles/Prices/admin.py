from django.contrib import admin
from Prices.models import prices

class AdminPrice(admin.ModelAdmin):
    list=('tilte','description')

# Register your models here.
admin.site.register(prices,AdminPrice)