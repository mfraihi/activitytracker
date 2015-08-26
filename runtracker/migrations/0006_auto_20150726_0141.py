# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('runtracker', '0005_auto_20150726_0140'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='run',
            name='runid',
        ),
        migrations.AddField(
            model_name='run',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, default=0, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='run',
            name='distance',
            field=models.FloatField(default=0),
        ),
    ]
