from django.urls import path
from rest_framework import routers
from .views import PersonViewSet

router = routers.SimpleRouter()

router.register(r'person', PersonViewSet)
