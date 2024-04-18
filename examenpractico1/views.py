from django.shortcuts import render
from rest_framework import viewsets
from .models import Transporte
from .serializer import TransporteSerializer
# Create your views here.

class TransporteViewset(viewsets.ModelViewSet):
    queryset= Transporte.objects.all()
    serializer_class= TransporteSerializer