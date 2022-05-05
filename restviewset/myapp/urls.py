from django.urls import path,include
from .views import *
from rest_framework.routers import DefaultRouter

# Creating Router Object
router = DefaultRouter()
# Register StudentViewSet with Router
router.register('studentapi', StudentViewSet, basename='student')

urlpatterns = [
 
    path('', include(router.urls)),

 
]
