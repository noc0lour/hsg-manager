# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('abbrev', models.CharField(max_length=50)),
                ('homepage', models.URLField(blank=True)),
                ('postbox', models.CharField(blank=True, max_length=3)),
                ('logo', models.FileField(blank=True, upload_to='Logos/')),
                ('members', models.SmallIntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='GroupContact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=75)),
                ('phone', models.CharField(max_length=15)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='GroupEmail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=75)),
                ('group', models.ForeignKey(related_name='listemail', to='hsg.Group')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PostAddress',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('street', models.CharField(max_length=50)),
                ('housenumber', models.CharField(max_length=10)),
                ('location', models.CharField(max_length=50)),
                ('zipcode', models.CharField(max_length=10)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RegInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('year', models.SmallIntegerField()),
                ('documents', models.BooleanField(default=0)),
                ('constitution', models.BooleanField(default=0)),
                ('comment', models.CharField(blank=True, max_length=160)),
                ('duedate', models.DateField(blank=True)),
                ('form', models.CharField(default='NONE', choices=[('FULL', 'Full'), ('PREL', 'Preliminary'), ('NONE', 'None')], max_length=4)),
                ('group', models.ForeignKey(related_name='registration', to='hsg.Group')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RegProcess',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('mailinglist', models.BooleanField(default=0)),
                ('homepage', models.BooleanField(default=0)),
                ('logowall', models.BooleanField(default=0)),
                ('group', models.ForeignKey(related_name='status', to='hsg.Group')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='groupcontact',
            name='address',
            field=models.ForeignKey(to='hsg.PostAddress'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='groupcontact',
            name='registration',
            field=models.ForeignKey(related_name='contact', to='hsg.RegInfo'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='group',
            name='address',
            field=models.ForeignKey(to='hsg.PostAddress', blank=True),
            preserve_default=True,
        ),
    ]
