from django.db import models

class Grocery(models.Model):
    name=models.CharField(max_length=100)
    quantity=models.IntegerField


class Budget(models.Model):
    name = models.CharField(max_length=100)
    amount = models.IntegerField()
    date=models.DateTimeField()

