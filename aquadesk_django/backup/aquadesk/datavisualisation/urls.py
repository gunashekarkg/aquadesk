from django.db import router
from django.urls import path
from django.urls.conf import include
from .views import LifeformSerializerViewSet,CountsessionSerializerViewSet,TankSerializerAPIView,TankSerializerAPI,CountsessionSerializerAPI
from rest_framework import renderers
from rest_framework.routers import DefaultRouter
# from . import views

# urlpatterns = [
#     path('lifeformapi',views.LifeformSerializerViewSet, name='lifeformapi'),
#     path('countsessionapi',views.CountsessionSerializerViewSet, name='Countsessionapi'),
#     path('tankapi',views.TankSerializerViewSet, name='tankapi'),
# ]
# router = DefaultRouter()
# router.register('lifeform',LifeformSerializerViewSet)
Lifeform_list = LifeformSerializerViewSet.as_view({'get': 'list'})
Countsession_list = CountsessionSerializerViewSet.as_view({'get': 'list'})
Tank_list = TankSerializerAPIView.as_view()

urlpatterns = [
    # path('lifeform/',include(router.urls)),
    path('lifeformapi',LifeformSerializerViewSet, name='lifeformapi'),
    path('countsessionapi',CountsessionSerializerViewSet, name='Countsessionapi'),
    path('tankapi',TankSerializerAPIView.as_view(), name='tankapi'),
    path('tankapi1',TankSerializerAPI, name='tankapi1'),
    path('countsessionapi1',CountsessionSerializerAPI, name='countsessionapi1'),
]