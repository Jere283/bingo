from rest_framework import serializers

from auth_u.models import User
from auth_u.serializers import UserRegisterSerializer
from .models import Participantes

class ParticipanteSerializer(serializers.ModelSerializer):
    entregado_por = UserRegisterSerializer(required=False, allow_null=True)

    class Meta:
        model = Participantes
        fields = '__all__'
        read_only_fields = ['entregado_por']

    def create(self, validated_data):
        entregado_por_data = validated_data.pop('entregado_por', None)
        participante = Participantes.objects.create(**validated_data)


        if entregado_por_data:
            participante.entregado_por = User.objects.get(id=entregado_por_data['id'])
            participante.save()

        return participante