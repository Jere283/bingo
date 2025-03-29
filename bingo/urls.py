from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ParticipanteViewSet, ver_qr, MarcarComoEntregado

router = DefaultRouter()
router.register(r'participantes', ParticipanteViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('participantes/<int:pk>/qr/', ver_qr, name='ver_qr'),
    path('participantes/<uuid:pk>/entregar/', MarcarComoEntregado.as_view(), name = 'entregar_carton')
]
