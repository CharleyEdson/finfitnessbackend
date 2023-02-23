from rest_framework import serializers
from .models import Currentincexp

class CurrentincexpflowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Currentincexp
        fields = ['current_income', 'id','year', 'date','user_id','month','current_expense']
        depth = 1