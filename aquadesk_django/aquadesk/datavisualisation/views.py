from django.db.models import Avg, Max, Min, Sum,Count,StdDev, F, Value,Q
from django.db.models.functions import Trunc, TruncDate
from django.db import connection
from django.db.models.expressions import ExpressionWrapper
from django.db.models.fields import FloatField, IntegerField
from django.db.models.query import Prefetch
from django.http import response
from django.shortcuts import render
from django_filters.rest_framework.filterset import FilterSet
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView
""" This script is used for creating the APIs. The rest framework provides views methods which are used for creating APIs.
The tables defined in models.py can only be used here with the serializers defined in serializers.py for API creation"""
from .serializers import (LifeformSerializers, TankSerializers,CountsessionSerializers,
                        TankSerializer,LifeformFlattenSerializer)
from .models import User, Tank, Countsession, CalibrationSizeWeightData, CalibrationSizeWeightModels, Lifeform
import requests
from rest_framework import viewsets
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import FilterSet
from django_filters import rest_framework as filters
from rest_flex_fields.views import FlexFieldsMixin
from rest_flex_fields import is_expanded

# def frontend(request):
#     """Vue.js will take care of everything else."""
#     lifeform = Lifeform.objects.all()
#     countsession = Countsession.objects.all()

#     data = {
#         'lifeform': lifeform,
#         'countsession': countsession,
#     }

#     return render(request, 'myapp/template.html', data)

# def test_vue(request):
#     return render(request, 'datavisualisation/test.html')

# Create views here.
CONSTANT_MEASUREMENTS =[{'Count':'Number_of_species'},{'Length':'Size_in_mm'},{'Weight':'Weight_in_gm'},{'Deformed':'Deformed'}]
SELECTED_FISH = [{'shrimps':'shrimps'},{'trouts':'trouts'}]
class LifeformSerializerViewSet(viewsets.ModelViewSet):
    """
    Initially created for ViewSet for viewing and editing lifeform table data without dynamic serialisation.
    """
    # queryset = Lifeform.objects.filter(type='shrimps').all()
    queryset = Lifeform.objects.order_by('id').all()
    serializer_class = LifeformSerializers

class CountsessionSerializerViewSet(viewsets.ModelViewSet):
    """
    Initially created for ViewSet for viewing and editing countsession table data without dynamic serialisation.
    """
    queryset = Countsession.objects.all()
    serializer_class = CountsessionSerializers

class TankSerializerAPIView(APIView):
    """
    Initially created for ViewSet for viewing and editing tank table data without dynamic serialisation.
    """
    def get(self, request):
        tanks = Tank.objects.filter(active=True)
        serializer = TankSerializers(tanks, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def TankSerializerAPI(request):
    """
    Initially created for Views for viewing tank table data without dynamic serialisation.
    """
    if request.method == "GET":
        results = Tank.objects.all()
        serializer = TankSerializers(results,many=True)
        return Response(serializer.data)

@api_view(['GET'])
def CountsessionSerializerAPI(request):
    """
    Initially created for Views for viewing countsession table data without dynamic serialisation.
    """
    if request.method == "GET":
        results = Countsession.objects.all()
        serializer = CountsessionSerializers(results,many=True)
        return Response(serializer.data)    

class LifeformModelViewSet(ModelViewSet):
    """
    A simple ViewSet for viewing and editing lifeform table data.
    """
    queryset = Lifeform.objects.all()
    serializer_class = LifeformSerializers





class AquaticFilter(FilterSet):
    type_filter = filters.CharFilter(method="filter_by_type")
    location = filters.CharFilter('location')
    population = filters.CharFilter('countsessiontotank__population')
    start = filters.CharFilter('countsessiontotank__start')
    length = filters.CharFilter('countsessiontotank__lifeformtocountsession__length')
    # id = filters.CharFilter('countsessiontotank__lifeformtocountsession__id')
    # type = filters.CharFilter('countsessiontotank__lifeformtocountsession__type')
    
    # type1=Tank.objects.filter(countsessiontotank__lifeformtocountsession =[{'id'}])
    class Meta:
        model = Tank
        fields = ('location','population','start','length')
        # fields = {
        #     'countsessiontotank': ['start', 'population'],
        #     'lifeformtocountsession': ['id', 'type'],
        # }


    def filter_by_type(self,queryset,name,value):
        # type_names = value.strip().split(",")
        # types = Tank.objects.filter(countsessiontotank__lifeformtocountsession__type__in=type_names)
        # queryset = queryset.filter(countsessiontotank__lifeformtocountsession__length_max__contains=value).distinct()
        # queryset = Tank.objects.prefetch_related(Prefetch('countsessiontotank__lifeformtocountsession', queryset=Lifeform.objects.filter(type=value).order_by('id').distinct()))
        # queryset = Tank.objects.prefetch_related(Prefetch('countsessiontotank__lifeformtocountsession', queryset=Lifeform.objects.filter(type=value).order_by('id').distinct()))
        # queryset = Tank.objects.prefetch_related(
        #                     Prefetch('countsessiontotank', queryset=Countsession.objects.filter(lifeformtocountsession__type=value).distinct()),
        #                     Prefetch('countsessiontotank__lifeformtocountsession', queryset=Lifeform.objects.all().order_by('id'))
        #                     )

        queryset = Tank.objects.prefetch_related(
            Prefetch('countsessiontotank', queryset=Countsession.objects.filter(lifeformtocountsession__type=value).distinct()),
            Prefetch('countsessiontotank__lifeformtocountsession', queryset=Lifeform.objects.filter(type=value).order_by('id').distinct()),)
        return queryset

        


class TankModelViewSet(ModelViewSet):
    """
    A simple ViewSet for viewing and editing tank table data.
    """
    queryset = Tank.objects.all()
    serializer_class = TankSerializers
    filter_backends = (DjangoFilterBackend,)
    filter_class = AquaticFilter
    # ordering = ('countsessiontotank__lifeformtocountsession__id')


class SummaryFilter(FilterSet):
    type_filter = filters.CharFilter(method="filter_by_type")

    def filter_by_type(self,queryset,name,value):
        queryset = Tank.objects.prefetch_related(
            Prefetch('countsessiontotank', queryset=Countsession.objects.filter(lifeformtocountsession__type=value).distinct()),
            Prefetch('countsessiontotank__lifeformtocountsession', queryset=Lifeform.objects.filter(type=value).order_by('id').distinct()),)
        return queryset

class SummaryModelViewSet(ModelViewSet):
    queryset = Tank.objects.all().filter(countsessiontotank__lifeformtocountsession__type='shrimps')
    serializer_class = TankSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_class = SummaryFilter

    def get_queryset(self):
        # queryset = Tank.objects.values('location').annotate(total_count=Count('countsessiontotank__lifeformtocountsession__deformed'), def_count = Count('countsessiontotank__lifeformtocountsession__deformed',filter=Q(countsessiontotank__lifeformtocountsession__deformed=True)))
        # queryset = queryset.annotate(def_percent = ExpressionWrapper(F('def_count')/F('total_count'), output_field=FloatField()))
        queryset = Tank.objects.values('location','countsessiontotank__start').annotate(total_count=Count('countsessiontotank__lifeformtocountsession__deformed'), def_count = Count('countsessiontotank__lifeformtocountsession__deformed',filter=Q(countsessiontotank__lifeformtocountsession__deformed=True))).values('location','countsessiontotank__start',def_percent = F('def_count')/F('total_count')*100).annotate(            
            counts = Count('countsessiontotank__lifeformtocountsession__deformed'),
            length_max=Max('countsessiontotank__lifeformtocountsession__length'),
            length_min=Min('countsessiontotank__lifeformtocountsession__length'),
            length_avg=Avg('countsessiontotank__lifeformtocountsession__length'),
            length_std=StdDev('countsessiontotank__lifeformtocountsession__length'),
            Num_of_not_sorted = Sum('countsessiontotank__num_not_sortable'),
            Date = TruncDate('countsessiontotank__start'),
            type = F('countsessiontotank__lifeformtocountsession__type')
        )

        return queryset


class SummaryTankModelViewSet(ModelViewSet):
    queryset = Tank.objects.all()
    serializer_class = TankSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_class = AquaticFilter

    def get_queryset(self):
        # queryset = Tank.objects.values('location').annotate(total_count=Count('countsessiontotank__lifeformtocountsession__deformed'), def_count = Count('countsessiontotank__lifeformtocountsession__deformed',filter=Q(countsessiontotank__lifeformtocountsession__deformed=True)))
        # queryset = queryset.annotate(def_percent = ExpressionWrapper(F('def_count')/F('total_count'), output_field=FloatField()))
        queryset = Tank.objects.values('location').annotate(total_count=Count('countsessiontotank__lifeformtocountsession__deformed'), def_count = Count('countsessiontotank__lifeformtocountsession__deformed',filter=Q(countsessiontotank__lifeformtocountsession__deformed=True))).values('location',def_percent = F('def_count')/F('total_count')*100).annotate(            
            counts = Count('countsessiontotank__lifeformtocountsession__deformed'),
            length_max=Max('countsessiontotank__lifeformtocountsession__length'),
            length_min=Min('countsessiontotank__lifeformtocountsession__length'),
            length_avg=Avg('countsessiontotank__lifeformtocountsession__length'),
            length_std=StdDev('countsessiontotank__lifeformtocountsession__length'),
            Num_of_not_sorted = Sum('countsessiontotank__num_not_sortable'),
            Date = TruncDate('countsessiontotank__start'),
            type = F('countsessiontotank__lifeformtocountsession__type')
        )

        return queryset




# class TankModelViewSets(ModelViewSet):
#     """
#     A simple ViewSet for viewing and editing tank table data.
#     """
#     queryset = Tank.objects.all()
#     serializer_class = TankSerializer
#     filter_backends = (DjangoFilterBackend,)
#     # filter_fields = ('location','countsessiontotank__lifeformtocountsession__type')
#     filter_class = AquaticFilter
#     ordering = ('countsessiontotank__lifeformtocountsession__id')

class CountsessionModelViewSet(ModelViewSet):
    """
    A simple ViewSet for viewing and editing countsession table data.
    """
    queryset = Countsession.objects.all()
    serializer_class = CountsessionSerializers


# class FishModelViewSet(ModelViewSet):
#     """
#     A simple ViewSet for viewing and editing type of aquatic species data.
#     """
#     queryset = Lifeform.objects.order_by().values('type').distinct()
#     serializer_class = FishSerializer


class SelectedFishModelViewSet(ModelViewSet):
    """
    A simple ViewSet for viewing and editing type of aquatic species data.
    """
    queryset = Lifeform.objects.filter(type='shrimps').all()
    serializer_class = LifeformSerializers



class AquaticFlattenFilter(FilterSet):
    type_filter = filters.CharFilter(method="filter_by_type")
    location = filters.CharFilter('location')
    population = filters.CharFilter('population')
    Date = filters.CharFilter('Date')
    length = filters.CharFilter('length')

    class Meta:
        model = Lifeform
        fields = ('location','population','Date','length')


    def filter_by_type(self,queryset,name,value):
        queryset = Lifeform.objects.filter(type=value).distinct()
        return queryset

class LifeformFlattenModelViewSet(ModelViewSet):
    """
    A simple ViewSet for viewing and editing lifeform table data.
    """
    queryset = Lifeform.objects.all()
    serializer_class = LifeformFlattenSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_class = AquaticFlattenFilter
