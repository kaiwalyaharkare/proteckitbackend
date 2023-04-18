from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from .serlizers import waitlistSerializer
from .models import waitlist
# Create your views here.
@api_view(['GET'])
def apiinfo(req):
    api_urls = {
        'all_items': '/all',
        'Add': '/create',
    }
    return Response(api_urls)
@api_view(['POST'])
def addtowailist(req):
    item = waitlistSerializer(data=req.data)
    if waitlist.objects.filter(**req.data).exists():
        raise serializers.ValidationError('This data already exists')
    if item.is_valid():
        item.save()
        return Response(item.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
