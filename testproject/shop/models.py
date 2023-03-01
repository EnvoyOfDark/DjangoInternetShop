from django.db import models


class Shop(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    date = models.DateField()
    price = models.FloatField()
    amount = models.IntegerField()