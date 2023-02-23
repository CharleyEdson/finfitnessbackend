from django.db import models
from authentication.models import User

# Create your models here.

class Liability(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type_of_liability = models.CharField(max_length=250)
    value = models.IntegerField()
    monthly_payment = models.IntegerField()
    date = models.DateField()