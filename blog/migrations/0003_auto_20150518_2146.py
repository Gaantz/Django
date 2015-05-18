# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20150518_1657'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tienda',
            name='latitud',
        ),
        migrations.RemoveField(
            model_name='tienda',
            name='longitud',
        ),
        migrations.AlterField(
            model_name='tienda',
            name='imagen',
            field=models.ImageField(upload_to=b'Tiendas'),
        ),
        migrations.AlterField(
            model_name='tienda',
            name='tipo',
            field=models.CharField(default=b'--ELIJA--', max_length=10, choices=[(b'mujer', b'MUJER'), (b'hombre', b'HOMBRE'), (b'mixta', b'MIXTA')]),
        ),
    ]
