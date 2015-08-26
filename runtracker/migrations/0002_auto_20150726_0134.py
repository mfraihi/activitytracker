# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('runtracker', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='run',
            old_name='id',
            new_name='run_id',
        ),
    ]
