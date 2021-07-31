from django.contrib import admin

# Register your models here.
from .models import User, Tank, SizeWeightModels, Countsession, SizeWeightData, Lifeform
# Register your models here.
admin.site.register(User)
admin.site.register(Tank)
admin.site.register(SizeWeightModels)
admin.site.register(Countsession)
admin.site.register(SizeWeightData)
admin.site.register(Lifeform)