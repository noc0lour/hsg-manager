# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hsg', '0003_auto_20150523_0019'),
    ]

    operations = [
        migrations.RenameField(
            model_name='postaddress',
            old_name='Group',
            new_name='group',
        ),
        migrations.RenameField(
            model_name='postaddress',
            old_name='Person',
            new_name='person',
        ),
    ]
