# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('runtracker', '0002_auto_20150726_0134'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='run',
            name='run_id',
        ),
        migrations.AddField(
            model_name='run',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, default=0, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]
