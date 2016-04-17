# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hsg', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='address',
            field=models.ForeignKey(null=True, blank=True, to='hsg.PostAddress'),
            preserve_default=True,
        ),
    ]
