from django.http import response
from django.shortcuts import redirect, render, HttpResponseRedirect
from django.http import HttpResponse, request
from .models import Ceo
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated

from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from  .serializers import CeoSerializer

# Create your views here.

@api_view(['GET'])
@authentication_classes([SessionAuthentication])
@permission_classes([IsAuthenticated])
def apiOverview(request):
    api_urls = {
        'List': '/task-list',
        'Detail View':'/task-detail/<str:pk>/',
        'Create':'/task-create/',
        'Update':'/task-update/<str:pk>/',
        'Delete':'/task-delete/<str:pk>/',
    }
    return Response(api_urls)

@api_view(['GET'])
@authentication_classes([SessionAuthentication])
@permission_classes([IsAuthenticated])
def taskList(request):
    tasks = Ceo.objects.all()
    serializer = CeoSerializer(tasks, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@authentication_classes([SessionAuthentication])
@permission_classes([IsAuthenticated])
def taskDetail(request, pk):
    tasks = Ceo.objects.get(id=pk)
    serializer = CeoSerializer(tasks, many=False)
    return Response(serializer.data)

@api_view(['POST'])
@authentication_classes([SessionAuthentication])
@permission_classes([IsAuthenticated])
def taskCreate(request):
    serializer = CeoSerializer(data=request.data)
    
    if serializer.is_valid():
        serializer.save()
    
    return Response(serializer.data)

@api_view(['POST'])
@authentication_classes([SessionAuthentication])
@permission_classes([IsAuthenticated])
def taskUpdate(request, pk):
    task = Ceo.objects.get(id=pk)
    serializer = CeoSerializer(instance=task, data=request.data)
    
    if serializer.is_valid():
        serializer.save()
    
    return Response(serializer.data)

@api_view(['DELETE'])
@authentication_classes([SessionAuthentication])
@permission_classes([IsAuthenticated])
def taskDelete(request, pk):
    task = Ceo.objects.get(id=pk)
    task.delete()

    return Response('Item successfully deleted!!')