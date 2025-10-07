from django.db import models

# Create your models here.
class rechargePlans(models.Model):
    planName = models.CharField(max_length=100)
    planPrice = models.IntegerField()
    planValidity = models.CharField(max_length=50)
    planStar = models.CharField(max_length=50)
    planData = models.CharField(max_length=50)
    ValidityDescription = models.TextField()
    planApi = models.CharField(max_length=100)  
    def __str__(self):
        return self.planName    