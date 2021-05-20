from django.shortcuts import render
from rest_framework import viewsets
from .models import Jedzenie
from .serializers import JedzenieSerializer


class JedzenieView(viewsets.ModelViewSet):
    queryset = Jedzenie.objects.all()
    serializer_class = JedzenieSerializer
