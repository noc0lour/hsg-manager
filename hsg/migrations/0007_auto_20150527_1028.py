# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hsg', '0006_auto_20150526_2226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groupcontact',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='groupemail',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]
