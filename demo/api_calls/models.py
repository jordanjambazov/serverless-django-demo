from django.db import models


class ApiCall(models.Model):
    num = models.IntegerField()
    time = models.DateTimeField(auto_now_add=True)
