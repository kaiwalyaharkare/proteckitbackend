from django.db.models import fields
from rest_framework import serializers
from .models import waitlist

class waitlistSerializer(serializers.ModelSerializer):
    class Meta:
        model= waitlist
        fields="__all__"