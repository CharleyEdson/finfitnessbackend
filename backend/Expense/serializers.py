from rest_framework import serializers
from .models import Expense

class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = ['id','type_of_expense', 'value','recurring', 'frequency', 'date', 'user_id']