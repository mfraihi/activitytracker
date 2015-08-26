# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('runtracker', '0008_run_duration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='run',
            name='duration',
            field=models.FloatField(default=0),
        ),
    ]
