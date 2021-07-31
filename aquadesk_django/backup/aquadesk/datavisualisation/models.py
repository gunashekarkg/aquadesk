from django.db import models

# Create your models here.

class User(models.Model):
    id = models.IntegerField(primary_key=True)
    password = models.CharField(max_length=40)
    email = models.CharField(max_length=100)

    class Meta:
        db_table = 'user'
        managed=False

class Tank(models.Model):
    id = models.IntegerField(primary_key=True)
    location = models.CharField(max_length=100)

    class Meta:
        db_table = 'tank'
        managed=False

class SizeWeightModels(models.Model):
    id = models.IntegerField(primary_key=True)
    model = models.CharField(max_length=100)

    class Meta:
        db_table = 'size_weight_model'
        managed=False

class Countsession(models.Model):
    id = models.IntegerField(primary_key=True)
    tank = models.ForeignKey(Tank,related_name='countsessiontotank',on_delete=models.SET_NULL, null=True)
    owner = models.ForeignKey(User,related_name='countsessiontouser',on_delete=models.SET_NULL, null=True)
    size_weight_model = models.ForeignKey(SizeWeightModels,related_name='countsessiontosizeweightmodel',on_delete=models.SET_NULL, null=True)
    start = models.DateTimeField(auto_now=True)
    population = models.IntegerField()

    class Meta:
        db_table = 'countsession'
        managed=False


class SizeWeightData(models.Model):
    id = models.IntegerField(primary_key=True)
    session = models.ForeignKey(Countsession,related_name='sizeweightdatatocountsession',on_delete=models.SET_NULL, null=True)
    weight = models.IntegerField()
    size = models.IntegerField()

    class Meta:
        db_table = 'size_weight_data'
        managed=False

class Lifeform(models.Model):
    id = models.IntegerField(primary_key=True)
    session = models.ForeignKey(Countsession,related_name='lifeformtocountsession',on_delete=models.SET_NULL, null=True)
    type = models.CharField(max_length=50)
    length_max = models.IntegerField()
    length_min = models.IntegerField()
    length_avg = models.IntegerField()
    length_std = models.IntegerField()

    class Meta:
        db_table = 'lifeform'
        managed=False