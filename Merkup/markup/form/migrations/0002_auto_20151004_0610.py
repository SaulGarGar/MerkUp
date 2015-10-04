# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.TextField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.TextField(default='', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='user_name',
            field=models.TextField(default='', max_length=30),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.TextField(max_length=30),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.TextField(max_length=30),
        ),
    ]
