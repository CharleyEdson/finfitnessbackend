from rest_framework import serializers
from .models import Budget

class budgetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Budget
        fields = ['id','budget_value', 'date', 'user_id']
        depth = 1