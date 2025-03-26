from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated

from registro.permissions import IsAdmin
from .models import Participantes
from .serializers import ParticipanteSerializer
from django.http import FileResponse, JsonResponse
from django.shortcuts import get_object_or_404

class ParticipanteViewSet(viewsets.ModelViewSet):
    queryset = Participantes.objects.all()
    serializer_class = ParticipanteSerializer
    permission_classes = [IsAdmin]
    filter_backends = [filters.SearchFilter]
    search_fields = ['telefono']


def ver_qr(request, pk):
    participante = get_object_or_404(Participantes, pk=pk)
    if participante.qr_code:
        return FileResponse(participante.qr_code.open(), content_type='image/png')
    return JsonResponse({'error': 'QR no encontrado'}, status=404)

