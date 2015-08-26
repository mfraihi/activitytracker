# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('runtracker', '0007_run_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='run',
            name='duration',
            field=models.TimeField(default=datetime.datetime(2015, 7, 26, 1, 49, 6, 178277, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
