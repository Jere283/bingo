# Generated by Django 5.1.7 on 2025-03-29 23:12

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bingo', '0006_rename_user_participantes_entregado_por'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='participantes',
            name='entregado_por',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
    ]
