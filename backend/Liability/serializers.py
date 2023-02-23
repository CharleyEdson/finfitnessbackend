from rest_framework import serializers
from .models import Liability

class LiabilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Liability
        fields = ['id','type_of_liability', 'value', 'monthly_payment','date', 'user_id']