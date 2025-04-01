from django.db import IntegrityError
from django.utils.timezone import make_aware
from rest_framework import viewsets, filters, status
from rest_framework.exceptions import ValidationError
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from auth_u.models import User
from registro.permissions import IsAdmin
from .models import Participantes
from .serializers import ParticipanteSerializer
from django.http import FileResponse, JsonResponse
from django.shortcuts import get_object_or_404

from datetime import datetime
import pytz



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

class MarcarComoEntregado(GenericAPIView):
    serializer_class = ParticipanteSerializer
    def post(self, request, pk):
        try:
            participante = get_object_or_404(Participantes, pk=pk)

            if participante.entregado:

                participante.entregado = False
                participante.fecha_entrega = None
                participante.entregado_por = None
                participante.save()
                serializer = self.serializer_class(instance=participante)

                return Response(data={
                    "data": serializer.data,
                    "message": "El carton del participante fue marcado como No entregado",
                }, status=status.HTTP_200_OK)

            usuario = User.objects.get(username=request.user.username)



            participante.entregado = True
            participante.fecha_entrega = datetime.now()
            participante.entregado_por = usuario
            participante.save()
            serializer = self.serializer_class(instance=participante)


            return Response(data={
                "data": serializer.data,
                "message": "El carton del participante fue marcado como entregado",
            }, status=status.HTTP_200_OK)

        except ValidationError as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

        except IntegrityError as e:
            return Response({"error": "A database integrity error occurred.", "details": str(e)},
                        status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:

            return Response({'error': 'An unexpected error occurred', 'details:':    str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
