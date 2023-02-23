from django.db import models
from authentication.models import User
from currentincexp.models import Currentincexp

# Create your models here.
class Cashflow(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    net_cash_flow = models.IntegerField()
    year = models.CharField(max_length=255)
    month = models.CharField(max_length=255)
    date = models.DateField()
    