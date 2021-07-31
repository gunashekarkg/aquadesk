from rest_framework import serializers
from .models import User, Tank, SizeWeightModels, Countsession, SizeWeightData, Lifeform



class TankSerializers(serializers.ModelSerializer):
    class Meta:
        model = Tank
        fields = ["location"]

class CountsessionSerializers(serializers.ModelSerializer):
    tank = TankSerializers(many=True, read_only=True)
    class Meta:
        model = Countsession
        fields = ["id","start","population","tank"]
        # fields = ["id","start","population"]

class LifeformSerializers(serializers.ModelSerializer):
    sessions = CountsessionSerializers(many=True, read_only=True)
    # session= serializers.SerializerMethodField()
    class Meta:
        model = Lifeform
        fields = ["length_max","length_min","length_avg","length_std","sessions"]


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