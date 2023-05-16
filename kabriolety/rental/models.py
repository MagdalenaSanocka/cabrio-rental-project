from django.db import models

class Car(models.Model):
    brand = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    year = models.IntegerField()
    body_type = models.CharField(max_length=20)
    power = models.IntegerField()
    seats = models.IntegerField()
    price_per_day = models.DecimalField(max_digits=6, decimal_places=2)

class Reservation(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
