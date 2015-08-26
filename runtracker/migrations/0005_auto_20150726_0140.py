# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('runtracker', '0004_auto_20150726_0138'),
    ]

    operations = [
        migrations.RenameField(
            model_name='run',
            old_name='run_id',
            new_name='runid',
        ),
    ]
