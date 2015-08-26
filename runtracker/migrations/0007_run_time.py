# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('runtracker', '0006_auto_20150726_0141'),
    ]

    operations = [
        migrations.AddField(
            model_name='run',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 26, 1, 46, 42, 324856, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
