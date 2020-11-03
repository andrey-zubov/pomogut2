# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medialibrary', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mediafile',
            name='categories',
            field=models.ManyToManyField(verbose_name='categories', blank=True, to='medialibrary.Category'),
        ),
        migrations.AddField(
            model_name='mediafile',
            name='copyright',
            field=models.CharField(verbose_name='copyright', max_length=200, blank=True),
        ),
    ]
