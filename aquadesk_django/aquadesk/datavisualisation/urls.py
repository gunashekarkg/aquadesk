from django.db import router
from django.urls import path
from django.urls.conf import include
from .views import (LifeformSerializerViewSet,CountsessionSerializerViewSet,
                    TankSerializerAPIView,TankSerializerAPI,CountsessionSerializerAPI,LifeformFlattenModelViewSet,
                    LifeformModelViewSet,SelectedFishModelViewSet,SummaryModelViewSet,SummaryTankModelViewSet,
                    TankModelViewSet,CountsessionModelViewSet)
from rest_framework import renderers
from rest_framework.routers import DefaultRouter

# from . import views
""" This script is used for creating the routered APIs with the help of ModelViewSet or static one is to one API using views.
The views defined in views.py can be used here for creating urls, that are used in front-end"""
#urls created for data visualisation tab of AquaDesk
router = DefaultRouter(trailing_slash=False)
router.register(r'tank', TankModelViewSet, basename='tank')
router.register(r'summary', SummaryModelViewSet, basename='summary')
router.register(r'summarytank', SummaryTankModelViewSet, basename='summarytank')
router.register(r'lifelorm', LifeformModelViewSet, basename='lifelorm')


# urlpatterns = router1.urls

# router2 = DefaultRouter(trailing_slash=False)
router.register(r'countsession', CountsessionModelViewSet, basename='countsession')
router.register(r'flatten', LifeformFlattenModelViewSet, basename='flatten')
# router.register(r'summary', SummaryModelViewSets, basename='summary')
router.register(r'selectedfishtype', SelectedFishModelViewSet, basename='selectedfishtype')

# urlpatterns = router2.urls

urlpatterns = [
    # path('lifeform/',include(router.urls)),
    path('lifeformapi',LifeformSerializerViewSet, name='lifeformapi'),
    path('countsessionapi',CountsessionSerializerViewSet, name='Countsessionapi'),
    path('tankapi',TankSerializerAPIView.as_view(), name='tankapi'),
    path('gettankapi',TankSerializerAPI, name='gettankapi'),
    path('getcountsessionapi',CountsessionSerializerAPI, name='getcountsessionapi'),
    # router2.urls,
    path('', include(router.urls)),
]