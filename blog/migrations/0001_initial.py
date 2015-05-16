# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ropa',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('talla', models.CharField(default=b'--ELIJA--', max_length=5, choices=[(b'XL', b'xl'), (b'L', b'l'), (b'M', b'm'), (b'S', b's')])),
                ('descripcion', models.TextField(max_length=100)),
                ('imagen', models.ImageField(upload_to=b'')),
            ],
            options={
                'db_table': 'Ropa',
            },
        ),
        migrations.CreateModel(
            name='Tienda',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('ruc', models.IntegerField()),
                ('tipo', models.CharField(default=b'--ELIJA--', max_length=10, choices=[(b'MUJER', b'mujer'), (b'HOMBRE', b'hombre'), (b'MIXTA', b'mixto')])),
                ('latitud', models.DecimalField(max_digits=10, decimal_places=5)),
                ('longitud', models.DecimalField(max_digits=10, decimal_places=5)),
                ('imagen', models.ImageField(upload_to=b'')),
            ],
            options={
                'db_table': 'Tienda',
            },
        ),
        migrations.AddField(
            model_name='ropa',
            name='tienda',
            field=models.ForeignKey(to='blog.Tienda'),
        ),
    ]
