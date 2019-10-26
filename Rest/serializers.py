from rest_framework import serializers

from Principal.models import PersonaMovil, AlertaPerona, Accidente
# from Accidente.models import Accidente

class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonaMovil
        fields = ('telefonoPer', 'nombrePer','correoPer')


class AlertaSerializer(serializers.ModelSerializer):
    # Persona = PersonaSerializer(read_only=True)
    # PersonaId = serializers.PrimaryKeyRelatedField(write_only=True, queryset=PersonaMovil.objects.all(), source='Persona', many=False)
    class Meta:
        model = AlertaPerona
        fields = ('telefonoPer', 'nombrePer','correoPer','tipoAccidente', 'latitud','longitud', 'ubicacion')


class AccidenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Accidente
        fields = '__all__'
