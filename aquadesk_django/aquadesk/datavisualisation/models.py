from django.db import models
from django.db.models.aggregates import Avg
""" This script is used for creating the tables in the db by importing models methods from django db
    The tables that are used in serializers.py and views.py are declared with the column names,  only these columns can be used further """

class User(models.Model):
#sync with user table in AquaData
# if table has not created, we can use this to create the table else just use the existing table structure
    id = models.IntegerField(primary_key=True)
    password = models.CharField(max_length=40)
    email = models.CharField(max_length=100)

    class Meta:
        db_table = 'user'
        managed=False # Control of tables are not provided to DRF

    # def __str__(self):
    #     return self.id


class Tank(models.Model):
#sync with tank table in AquaData
# if table has not created, we can use this to create the table else just use the existing table structure
    id = models.IntegerField(primary_key=True)
    location = models.CharField(max_length=100)
    owner = models.ForeignKey(User,related_name='tanktouser',on_delete=models.CASCADE, null=False)

    class Meta:
        db_table = 'tank'
        managed=False
    
    # def __str__(self):
    #     return self.id


class CalibrationSizeWeightModels(models.Model):
#sync with size_weight_model table in AquaData
# if table has not created, we can use this to create the table else just use the existing table structure
    id = models.IntegerField(primary_key=True)
    model = models.CharField(max_length=100)

    class Meta:
        db_table = 'calibration_size_weight_model'
        managed=False

    # def __str__(self):
    #     return self.id


class Countsession(models.Model):
#sync with Countsession table in AquaData
# if table has not created, we can use this to create the table else just use the existing table structure
    id = models.IntegerField(primary_key=True)
    tank = models.ForeignKey(Tank,related_name='countsessiontotank',on_delete=models.CASCADE, null=False)
    # owner = models.ForeignKey(User,related_name='countsessiontouser',on_delete=models.SET_NULL, null=True)
    model = models.ForeignKey(CalibrationSizeWeightModels,related_name='countsessiontosizeweightmodel',on_delete=models.CASCADE, null=False)
    start = models.DateField(auto_now=False)
    population = models.IntegerField()
    num_not_sortable = models.IntegerField()

    class Meta:
        db_table = 'countsession'
        managed=False

    # def __str__(self):
    #     return self.id


class CalibrationSizeWeightData(models.Model):
#sync with size_weight_data table in AquaData
# if table has not created, we can use this to create the table else just use the existing table structure
    id = models.IntegerField(primary_key=True)
    session = models.ForeignKey(Countsession,related_name='sizeweightdatatocountsession',on_delete=models.CASCADE, null=False)
    weight = models.IntegerField()
    size = models.IntegerField()

    class Meta:
        db_table = 'calibration_size_weight_data'
        managed=False

    # def __str__(self):
    #     return self.id


class Lifeform(models.Model):
#sync with lifeform table in AquaData 
# if table has not created, we can use this to create the table else just use the existing table structure
    id = models.IntegerField(primary_key=True)
    session = models.ForeignKey(Countsession,related_name='lifeformtocountsession',on_delete=models.CASCADE, null=False)
    type = models.CharField(max_length=100)
    deformed = models.BooleanField()
    length = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = 'lifeform'
        managed=False

    # def __str__(self):
    #     return self.id