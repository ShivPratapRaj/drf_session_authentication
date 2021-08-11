from django.db import models
from rest_framework import serializers
from .models import Ceo

class CeoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ceo
        fields = '__all__'