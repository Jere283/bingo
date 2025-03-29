from rest_framework import serializers

from auth_u.serializers import UserRegisterSerializer
from .models import Participantes

class ParticipanteSerializer(serializers.ModelSerializer):

    entregado_por = UserRegisterSerializer()
    class Meta:
        model = Participantes
        fields = '__all__'
