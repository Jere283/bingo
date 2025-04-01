import pytz
from rest_framework import serializers

from auth_u.models import User
from auth_u.serializers import UserRegisterSerializer
from .models import Participantes

class ParticipanteSerializer(serializers.ModelSerializer):
    entregado_por = UserRegisterSerializer(required=False, allow_null=True)
    fecha_entrega = serializers.SerializerMethodField()

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

    def get_fecha_entrega(self, obj):
        """Convierte la fecha_entrega a GMT-6 antes de devolverla."""
        if obj.fecha_entrega:
            gmt_6 = pytz.timezone("America/Guatemala")  # O "America/Mexico_City"
            return obj.fecha_entrega.astimezone(gmt_6).isoformat()
        return None