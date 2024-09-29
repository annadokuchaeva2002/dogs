from django.db import models


class Strolls(models.Model):
    apartment_number = models.IntegerField()
    animal_name = models.CharField(max_length=50)
    day = models.DateField()
    time_in_day = models.CharField(max_length=50)
