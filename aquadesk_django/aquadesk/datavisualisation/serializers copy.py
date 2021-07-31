from rest_framework import serializers
from rest_framework.serializers import SerializerMethodField
from .models import User, Tank, SizeWeightModels, Countsession, SizeWeightData, Lifeform

# class DynamicFieldsModelSerializer(serializers.ModelSerializer):


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

class LifeformSerializers(serializers.ModelSerializer):

    """
    A ModelSerializer that takes an additional `fields` argument that
    controls which fields should be displayed.
    """
    def __init__(self, *args, **kwargs):
        # Don't pass the 'fields' arg up to the superclass
        fields = kwargs.pop('fields', None)

        # Instantiate the superclass normally
        super(LifeformSerializers, self).__init__(*args, **kwargs)

        if fields is not None:
            # Drop any fields that are not specified in the `fields` argument.
            allowed = set(fields)
            existing = set(self.fields)
            for field_name in existing - allowed:
                self.fields.pop(field_name)
                
    class Meta:
        model = Lifeform
        fields = ["deformed","length_max","length_min","length_avg","length_std"]

class CountsessionSerializers(serializers.ModelSerializer):

    """
    A ModelSerializer that takes an additional `fields` argument that
    controls which fields should be displayed.
    """
    def __init__(self, *args, **kwargs):
        # Don't pass the 'fields' arg up to the superclass
        request = kwargs.get('context', {}).get('request')
        str_fields = request.GET.get('fields', '') if request else None
        fields = str_fields.split(',') if str_fields else None

        # Instantiate the superclass normally
        super(CountsessionSerializers, self).__init__(*args, **kwargs)

        if fields is not None:
            # Drop any fields that are not specified in the `fields` argument.
            allowed = set(fields)
            existing = set(self.fields)
            for field_name in existing - allowed:
                self.fields.pop(field_name)
    
    # lifeformtocountsession = LifeformSerializers(many=True, read_only=True)
    lifeformtocountsession = SerializerMethodField("get_lifeformtocountsession_serializer")
    class Meta:
        model = Countsession
        fields = ["id","start","population","lifeformtocountsession"]
        # fields = ["id","start","population"]

    def get_lifeformtocountsession_serializer(self, obj):
        request = self.context.get('request')
        serializer_context = {'request': request }
        lifeformtocountsession = obj.lifeformtocountsession.all()
        serializer = LifeformSerializers(lifeformtocountsession, many=True, context=serializer_context)
        return serializer.data
        
class TankSerializers(serializers.ModelSerializer):

    """
    A ModelSerializer that takes an additional `fields` argument that
    controls which fields should be displayed.
    """
    def __init__(self, *args, **kwargs):
        # Don't pass the 'fields' arg up to the superclass
        request = kwargs.get('context', {}).get('request')
        str_fields = request.GET.get('fields', '') if request else None
        fields = str_fields.split(',') if str_fields else None

        # Instantiate the superclass normally
        super(TankSerializers, self).__init__(*args, **kwargs)

        if fields is not None:
            # Drop any fields that are not specified in the `fields` argument.
            allowed = set(fields)
            existing = set(self.fields)
            for field_name in existing - allowed:
                self.fields.pop(field_name)
    # countsessiontotank = CountsessionSerializers(many=True, read_only=True)
    countsessiontotank = SerializerMethodField("get_countsessiontotank_serializer")
    class Meta:
        model = Tank
        fields = ["location","countsessiontotank"]

    
    def get_countsessiontotank_serializer(self, obj):
        request = self.context.get('request')
        serializer_context = {'request': request }
        countsessiontotank = obj.countsessiontotank.all()
        serializer = CountsessionSerializers(countsessiontotank, many=True, context=serializer_context)
        return serializer.data

class FishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lifeform
        fields = ["type"]

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