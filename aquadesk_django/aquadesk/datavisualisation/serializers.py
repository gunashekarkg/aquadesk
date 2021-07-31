from rest_framework import serializers
from django.db.models import Avg, Max, Min, Sum,Count,StdDev, F, Value
from rest_framework.serializers import SerializerMethodField
from .models import User, Tank, Countsession, CalibrationSizeWeightData, CalibrationSizeWeightModels, Lifeform
from django_restql.mixins import DynamicFieldsMixin
""" This script is used for creating the serializers, inturn used to convert data from db to JSON format, and JSON format data into db storable format. The rest framework provides serializers methods which are used for creating APIs.
The tables defined in models.py can only be used here"""
from rest_flex_fields import FlexFieldsModelSerializer
""" rest_flex_fields is a package used for fetching dynamic serialisers, inturn use these in APIs"""

class LifeformSerializers(FlexFieldsModelSerializer):
#To convert data from lifeform table to JSON format
    class Meta:
        model = Lifeform
        fields = ["id","length","deformed","type"]


class CountsessionSerializers(FlexFieldsModelSerializer):
#To convert data from countsession table to JSON format
    class Meta:
        model = Countsession
        fields = ["start","population"]
        expandable_fields = {
          'lifeformtocountsession': (LifeformSerializers, {'many': True})
        }


class TankSerializers(FlexFieldsModelSerializer):
#To convert data from tank table to JSON format
  # countsessiontotank = serializers.PrimaryKeyRelatedField(read_only=True)
  class Meta:
      model = Tank
      fields = ["location"]
      expandable_fields = {
        'countsessiontotank': (CountsessionSerializers, {'many': True})
      }



class LifeformSerializer(FlexFieldsModelSerializer):
#To convert data from lifeform table to JSON format
    class Meta:
        model = Lifeform
        fields = ["type"]


class CountsessionSerializer(FlexFieldsModelSerializer):
#To convert data from countsession table to JSON format
    class Meta:
        model = Countsession
        fields = ["start","population"]
        expandable_fields = {
          'lifeformtocountsession': (LifeformSerializer, {'many': True})
        }

class TankSerializer(FlexFieldsModelSerializer):
#To convert data from tank table to JSON format
  # countsessiontotank = serializers.PrimaryKeyRelatedField(read_only=True)
  length_max = serializers.DecimalField(max_digits=10, decimal_places=2)
  length_min = serializers.DecimalField(max_digits=10, decimal_places=2)
  length_avg = serializers.DecimalField(max_digits=10, decimal_places=2)
  length_std = serializers.DecimalField(max_digits=10, decimal_places=2)
  def_percent = serializers.IntegerField()
  counts = serializers.IntegerField()
  Num_of_not_sorted = serializers.IntegerField()
  Date = serializers.DateField()
  type = serializers.CharField()
  # total_pop = serializers.IntegerField()
  class Meta:
      model = Tank
      fields = ["Date","location","type","def_percent","length_max","length_min","length_avg","length_std","Num_of_not_sorted","counts"]
      expandable_fields = {
        'countsessiontotank': (CountsessionSerializer, {'many': True})
      }



"""Flatten Serialiser for Overview Table"""
class LifeformFlattenSerializer(FlexFieldsModelSerializer):
#To convert data from lifeform table to JSON format
  location = serializers.SerializerMethodField()
  Date = serializers.SerializerMethodField()
  class Meta:
      model = Lifeform
      fields = ["id","length","deformed","type","location","Date"]

  def get_location(self,obj):
    return obj.session.tank.location

  def get_Date(self,obj):
    return obj.session.start





# class LifeformSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
# #To convert data from lifeform table to JSON format
#     class Meta:
#         model = Lifeform
#         fields = ["id","length_max","length_min","length_avg","length_std","deformed"]


# class CountsessionSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
# #To convert data from countsession table to JSON format
#   lifeformtocountsession = LifeformSerializer(many=True, read_only=True)
#   class Meta:
#       model = Countsession
#       fields = ["start","population","lifeformtocountsession"]

# class TankSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
# #To convert data from tank table to JSON format
#   # countsessiontotank = serializers.PrimaryKeyRelatedField(read_only=True)
#   countsessiontotank = CountsessionSerializer(many=True, read_only=True) 
#   class Meta:
#       model = Tank
#       fields = ["location","countsessiontotank"]


"""Dynamic Serialisers wihout use of packages"""
#  class DynamicFieldsModelSerializer(serializers.ModelSerializer):
#     """
#     A ModelSerializer that takes an additional `fields` argument that
#     controls which fields should be displayed.
#     """

#     def __init__(self, *args, **kwargs):
#         # Don't pass the 'fields' arg up to the superclass
#         fields = kwargs.pop('fields', None)

#         # Instantiate the superclass normally
#         super(DynamicFieldsModelSerializer, self).__init__(*args, **kwargs)

#         if fields is not None:
#             # Drop any fields that are not specified in the `fields` argument.
#             allowed = set(fields)
#             existing = set(self.fields)
#             for field_name in existing - allowed:
#                 self.fields.pop(field_name)

# class LifeformSerializer(serializers.ModelSerializer):

#     """
#     A ModelSerializer that takes an additional `fields` argument that
#     controls which fields should be displayed.
#     """
#     def __init__(self, *args, **kwargs):
#         # Don't pass the 'fields' arg up to the superclass
#         fields = kwargs.pop('fields', None)

#         # Instantiate the superclass normally
#         super(LifeformSerializer, self).__init__(*args, **kwargs)

#         if fields is not None:
#             # Drop any fields that are not specified in the `fields` argument.
#             allowed = set(fields)
#             existing = set(self.fields)
#             for field_name in existing - allowed:
#                 self.fields.pop(field_name)
                
#     class Meta:
#         model = Lifeform
#         fields = ["deformed","length_max","length_min","length_avg","length_std"]

# class CountsessionSerializer(serializers.ModelSerializer):

#     """
#     A ModelSerializer that takes an additional `fields` argument that
#     controls which fields should be displayed.
#     """
#     def __init__(self, *args, **kwargs):
#         # Don't pass the 'fields' arg up to the superclass
#         request = kwargs.get('context', {}).get('request')
#         str_fields = request.GET.get('fields', '') if request else None
#         fields = str_fields.split(',') if str_fields else None

#         # Instantiate the superclass normally
#         super(CountsessionSerializer, self).__init__(*args, **kwargs)

#         if fields is not None:
#             # Drop any fields that are not specified in the `fields` argument.
#             allowed = set(fields)
#             existing = set(self.fields)
#             for field_name in existing - allowed:
#                 self.fields.pop(field_name)
    
#     # lifeformtocountsession = LifeformSerializers(many=True, read_only=True)
#     lifeformtocountsession = SerializerMethodField("get_lifeformtocountsession_serializer")
#     class Meta:
#         model = Countsession
#         fields = ["id","start","population","lifeformtocountsession"]
#         # fields = ["id","start","population"]

#     def get_lifeformtocountsession_serializer(self, obj):
#         request = self.context.get('request')
#         serializer_context = {'request': request }
#         lifeformtocountsession = obj.lifeformtocountsession.all()
#         serializer = LifeformSerializer(lifeformtocountsession, many=True, context=serializer_context)
#         return serializer.data
        
# class TankSerializer(serializers.ModelSerializer):

#     """
#     A ModelSerializer that takes an additional `fields` argument that
#     controls which fields should be displayed.
#     """
#     def __init__(self, *args, **kwargs):
#         # Don't pass the 'fields' arg up to the superclass
#         request = kwargs.get('context', {}).get('request')
#         str_fields = request.GET.get('fields', '') if request else None
#         fields = str_fields.split(',') if str_fields else None

#         # Instantiate the superclass normally
#         super(TankSerializer, self).__init__(*args, **kwargs)

#         if fields is not None:
#             # Drop any fields that are not specified in the `fields` argument.
#             allowed = set(fields)
#             existing = set(self.fields)
#             for field_name in existing - allowed:
#                 self.fields.pop(field_name)
#     # countsessiontotank = CountsessionSerializers(many=True, read_only=True)
#     countsessiontotank = SerializerMethodField("get_countsessiontotank_serializer")
#     class Meta:
#         model = Tank
#         fields = ["location","countsessiontotank"]

    
#     def get_countsessiontotank_serializer(self, obj):
#         request = self.context.get('request')
#         serializer_context = {'request': request }
#         countsessiontotank = obj.countsessiontotank.all()
#         serializer = CountsessionSerializer(countsessiontotank, many=True, context=serializer_context)
#         return serializer.data

# class FishSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Lifeform
#         fields = ["type"]
"""Static Serialisers, using the django rest framework packages"""
# class LifeformSerializers(serializers.ModelSerializer):
#     # sessions = CountsessionSerializers(many=True, read_only=True)
#     # session= serializers.SerializerMethodField()
#     class Meta:
#         model = Lifeform
#         fields = ["length_max","length_min","length_avg","length_std"]


# class AquaticSpeciesDataModelSerializer(serializers.ModelSerializer):
#     # sessions = CountsessionSerializer(many=True)
#     session= serializers.SerializerMethodField()
#     class Meta:
#         model = lifeform
#         fields = ["length_max","length_min","length_avg","length_std","session"]

#     def get_session(self,obj):
#         for x in obj.session:
#          print( x,"jgjhgjgdgdfg")
#         return [{'id':x.id} for x in obj]

