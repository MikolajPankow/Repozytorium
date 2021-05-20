from rest_framework import serializers
from .models import Jedzenie


class JedzenieSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Jedzenie
        fields = ('id', 'url', 'name', 'paradigm')
