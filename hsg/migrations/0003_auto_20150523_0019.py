# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hsg', '0002_auto_20150522_2336'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='address',
        ),
        migrations.RemoveField(
            model_name='group',
            name='members',
        ),
        migrations.RemoveField(
            model_name='groupcontact',
            name='address',
        ),
        migrations.AddField(
            model_name='postaddress',
            name='Group',
            field=models.ForeignKey(to='hsg.Group', related_name='address', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='postaddress',
            name='Person',
            field=models.ForeignKey(to='hsg.GroupContact', related_name='address', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='reginfo',
            name='members',
            field=models.SmallIntegerField(default=0),
            preserve_default=False,
        ),
    ]
