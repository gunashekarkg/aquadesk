from django.db.models import Avg, Max, Min, Sum
from django.db import connection
from django.http import response
from django.shortcuts import render
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView

from .serializers import LifeformSerializers, TankSerializers,CountsessionSerializers
from .models import User, Tank, SizeWeightModels, Countsession, SizeWeightData, Lifeform
import requests
from rest_framework import viewsets

# Create your views here.
class LifeformSerializerViewSet(viewsets.ModelViewSet):
    queryset = Lifeform.objects.all()
    serializer_class = LifeformSerializers

class CountsessionSerializerViewSet(viewsets.ModelViewSet):
    queryset = Countsession.objects.all()
    serializer_class = CountsessionSerializers

class TankSerializerAPIView(APIView):

    def get(self, request):
        tanks = Tank.objects.filter(active=True)
        serializer = TankSerializers(tanks, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def TankSerializerAPI(request):
    if request.method == "GET":
        results = Tank.objects.all()
        serializer = TankSerializers(results,many=True)
        return Response(serializer.data)

@api_view(['GET'])
def CountsessionSerializerAPI(request):
    if request.method == "GET":
        results = Countsession.objects.all()
        serializer = CountsessionSerializers(results,many=True)
        return Response(serializer.data)    


# class TankSerializerViewSet(viewsets.ModelViewSet):
#     queryset = Tank.objects.all()
#     serializer_class = TankSerializers


# class tankapi(viewsets.ModelViewSet):
#     queryset = tank.objects.all()
#     serializer_class = TankSerializer

# class countsessionapi(viewsets.ModelViewSet):
#     queryset = countsession.objects.all()
#     serializer_class = CountsessionSerializer

# class lifeformapi(viewsets.ModelViewSet):
#     queryset = lifeform.objects.all()
#     serializer_class = AquaticSpeciesDataModelSerializer

# class lifeformapi(APIView):
#     def get(self,request,*args,**kwargs):
#         results = lifeform.objects.all()
#         serializer = AquaticSpeciesDataModelSerializer(results,many=True)
#         return Response(serializer.data)

# life_form_api=lifeformapi.as_view()