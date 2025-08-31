from signal import default_int_handler
from django.db import models
from  tinymce.models import HTMLField

# Create your models here.
class ourService(models.Model):
    servicesTitle  = models.CharField(max_length=500)
    serviceDesc    = models.CharField(max_length=500)
    Descritionval  = HTMLField(default="Default description")
    Our_image      = models.FileField(upload_to="new/",max_length=250,default = None)
    # Our_image      = models.FileField(upload_to="new/",max_length=250,null=True,default = None,blank=True)
