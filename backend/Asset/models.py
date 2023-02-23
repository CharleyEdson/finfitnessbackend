from django.db import models
from authentication.models import User

# Create your models here.

class Asset(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    asset_type = models.CharField(max_length=255)
    value = models.IntegerField()
    date = models.DateField()