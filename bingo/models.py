import uuid

from django.db import models

class Participantes(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre = models.CharField(max_length=200)
    telefono = models.CharField(unique=True, max_length=20)
    carrera = models.CharField(max_length=200, blank=True, null=True)
    no_cuenta = models.CharField(unique=True, max_length=11, blank=True, null=True)
    correo = models.EmailField(unique=True, max_length=150, blank=True, null=True)
    pagado = models.BooleanField(blank=True, null=True)
    cartones = models.IntegerField()
    entregado = models.BooleanField()
    fecha_entrega = models.DateTimeField(blank=True, null=True)
    qr_code = models.ImageField(upload_to='qr_codes/', blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.qr_code:
            from io import BytesIO
            import qrcode
            from django.core.files.base import ContentFile

            qr = qrcode.make(self.id)
            buffer = BytesIO()
            qr.save(buffer, format="PNG")
            self.qr_code.save(f"{self.id}.png", ContentFile(buffer.getvalue()), save=False)

        super().save(*args, **kwargs)

    class Meta:
        db_table = 'participantes'
