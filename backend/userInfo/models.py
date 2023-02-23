from django.db import models
from authentication.models import User


# Create your models here.

class userInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=50)
    age = models.IntegerField()
    gender = models.CharField(max_length=50)
    occupation = models.CharField(max_length=50)
    risk_level = models.IntegerField()
    state_living_in = models.CharField(max_length=50)
    relationship_status = models.CharField(max_length=50)
    verified_facts = models.BooleanField()




", on_delete=models.CASCADE, null=True, blank=True"