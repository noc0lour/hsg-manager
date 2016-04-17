# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hsg', '0007_auto_20150527_1028'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reginfo',
            old_name='year',
            new_name='date',
        ),
    ]
