from django.db import models

# Create your models here.

class Run(models.Model):
    #run_id = models.AutoField(default=0)
    distance = models.FloatField(default=0)
    time = models.DateTimeField(auto_now = False, auto_now_add = False)

    duration = models.FloatField(default=0)
