from django.db import models
from authentication.models import User

# Create your models here.

class Expense(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type_of_expense = models.CharField(max_length=250)
    recurring = models.BooleanField(default=True)
    frequency = models.CharField(max_length=255, default='Monthly')
    value = models.IntegerField()
    date = models.DateField()