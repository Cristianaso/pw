# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resultados', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resultado',
            name='golesLocal',
            field=models.CharField(default=b'?', max_length=10),
        ),
        migrations.AlterField(
            model_name='resultado',
            name='golesVisitante',
            field=models.CharField(default=b'?', max_length=10),
        ),
    ]
