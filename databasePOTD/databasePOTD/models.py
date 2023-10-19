from django.db import models

class Friend(models.Model):
    name = models.CharField(max_length=50)
    major = models.CharField(max_length=50)
    year = models.IntegerField()


