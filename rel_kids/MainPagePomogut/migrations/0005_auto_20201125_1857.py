# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MainPagePomogut', '0004_mainpageblock_bitrix'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mainpageblock',
            options={'verbose_name': 'Блок главной страницы', 'verbose_name_plural': 'Блоки главной страницы'},
        ),
        migrations.AddField(
            model_name='mainpageblock',
            name='website',
            field=models.CharField(verbose_name='сайт', max_length=256, default=11),
            preserve_default=False,
        ),
    ]
