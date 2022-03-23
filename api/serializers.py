from attr import fields
from rest_framework_json_api import serializers
from dishes.models import Burger, Salad


class BurgerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Burger
        fields = ('name', 'price')


class SaladSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Salad
        fields = ('name', 'price')




