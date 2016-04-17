# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hsg', '0005_auto_20150526_1551'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reginfo',
            name='year',
            field=models.DateField(),
            preserve_default=True,
        ),
    ]
