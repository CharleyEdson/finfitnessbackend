from rest_framework import serializers
from .models import Asset

class AssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asset
        fields = ['id','asset_type', 'value', 'date','user_id']
        depth = 1