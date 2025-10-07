
from django.db import models
# from tinymce.models import HTMLField

# Create your models here.
class collectFormData(models.Model):
    userName = models.CharField(max_length=250)
    userEmail = models.CharField(max_length= 250)
    userMess =  models.CharField(max_length= 250)