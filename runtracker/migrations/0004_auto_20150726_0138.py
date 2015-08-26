# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('runtracker', '0003_auto_20150726_0136'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='run',
            name='id',
        ),
        migrations.AddField(
            model_name='run',
            name='run_id',
            field=models.AutoField(default=0, serialize=False, primary_key=True),
        ),
    ]
