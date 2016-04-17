# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hsg', '0004_auto_20150523_0020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reginfo',
            name='duedate',
            field=models.DateField(blank=True, null=True),
            preserve_default=True,
        ),
    ]
