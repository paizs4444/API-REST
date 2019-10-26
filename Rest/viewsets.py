from django.shortcuts import render


from rest_framework import viewsets

from .serializers import PersonaSerializer, AlertaSerializer, AccidenteSerializer
from Principal.models import PersonaMovil, AlertaPerona, Accidente
# from Accidente.models import Accidente
# Create your views here.

class PersonaViewSet(viewsets.ModelViewSet):
    queryset = PersonaMovil.objects.all().order_by('telefonoPer')
    serializer_class = PersonaSerializer

class AlertaViewSet(viewsets.ModelViewSet):
    queryset = AlertaPerona.objects.all().order_by('tipoAccidente')
    serializer_class = AlertaSerializer

class AccidenteViewSet(viewsets.ModelViewSet):
    queryset = Accidente.objects.all()
    serializer_class = AccidenteSerializer
