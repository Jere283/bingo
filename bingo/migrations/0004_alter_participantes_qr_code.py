# Generated by Django 5.1.7 on 2025-03-29 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bingo', '0003_alter_participantes_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participantes',
            name='qr_code',
            field=models.URLField(blank=True, null=True),
        ),
    ]
