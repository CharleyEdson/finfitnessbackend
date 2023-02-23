from rest_framework import serializers
from .models import Income

class IncomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Income
        fields = ['id','income_type', 'value', 'recurring', 'frequency', 'date', 'user_id']