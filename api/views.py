from django.shortcuts import render

from dishes.models import Burger, Salad
from . import serializers

from rest_framework import viewsets


class BurgerViewSet(viewsets.ModelViewSet):
    queryset = Burger.objects.all()
    serializer_class = serializers.BurgerSerializer


class SaladViewSet(viewsets.ModelViewSet):
    queryset = Salad.objects.all()
    serializer_class = serializers.SaladSerializer


