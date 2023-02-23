from rest_framework import serializers
from .models import Cashflow

class CashflowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cashflow
        fields = ['year','date', 'month','net_cash_flow', 'id','user_id']
        depth = 1