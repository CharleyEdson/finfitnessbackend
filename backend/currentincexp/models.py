from django.db import models
from authentication.models import User

# Create your models here.
class Currentincexp(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    current_income = models.IntegerField()
    current_expense = models.IntegerField()
    year = models.CharField(max_length=255)
    month = models.CharField(max_length=255)
    date = models.DateField()
    
    