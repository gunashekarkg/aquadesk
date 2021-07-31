from django.contrib import admin
"""This script is used to access the tables from admin pannel,  to add data o database with admin login.
    The models registered under this script can only be accessed by admin"""

from .models import User, Tank, CalibrationSizeWeightModels, Countsession, CalibrationSizeWeightData, Lifeform
# Registered models to admim here.
admin.site.register(User)
admin.site.register(Tank)
admin.site.register(CalibrationSizeWeightModels)
admin.site.register(Countsession)
admin.site.register(CalibrationSizeWeightData)
admin.site.register(Lifeform)