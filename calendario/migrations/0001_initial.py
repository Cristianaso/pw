# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Equipo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombreEquipo', models.CharField(max_length=20)),
                ('nombreEntrenador', models.CharField(max_length=50)),
                ('puesto', models.IntegerField(default=1)),
                ('puntos', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Partido',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateField()),
                ('hora', models.TimeField()),
                ('nombreLocal', models.CharField(max_length=20)),
                ('nombreVisitante', models.CharField(max_length=20)),
                ('equipoLocal', models.ForeignKey(to='calendario.Equipo')),
            ],
        ),
    ]
