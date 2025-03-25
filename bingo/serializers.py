from rest_framework import serializers
from .models import Participantes

class ParticipanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participantes
        fields = '__all__'
