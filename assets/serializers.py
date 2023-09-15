from rest_framework import serializers
from .models import Assets, CheckOutLog

class AssetsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assets
        fields = '__all__'

class CheckOutLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = CheckOutLog
        fields = '__all__'
