import uuid
from io import BytesIO

import cloudinary.uploader
import cloudinary.api
import qrcode
from dotenv import load_dotenv
load_dotenv()

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
    qr_code = models.URLField(blank=True, null=True)

    def save(self, *args, **kwargs):
        config = cloudinary.config(secure=True)
        if not self.qr_code:
            buffer = BytesIO()
            qr = qrcode.make(str(self.id))
            qr.save(buffer, format="PNG")
            buffer.seek(0)


            response = cloudinary.uploader.upload(
                buffer,
                public_id=f"qr_codes/{self.telefono}",
                unique_filename=True,
                overwrite=True
            )

            print(response)
            self.qr_code = response["secure_url"]

        super().save(*args, **kwargs)

    class Meta:
        db_table = 'participantes'
