# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MainPagePomogut', '0003_auto_20201121_0907'),
    ]

    operations = [
        migrations.AddField(
            model_name='mainpageblock',
            name='bitrix',
            field=models.CharField(max_length=256, blank=True, null=True),
        ),
    ]
