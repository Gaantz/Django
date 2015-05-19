# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20150518_2146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ropa',
            name='imagen',
            field=models.ImageField(upload_to=b'Ropas'),
        ),
        migrations.AlterField(
            model_name='ropa',
            name='talla',
            field=models.CharField(default=b'--ELIJA--', max_length=5, choices=[(b'xl', b'XL'), (b'l', b'L'), (b'm', b'M'), (b's', b'S')]),
        ),
    ]
