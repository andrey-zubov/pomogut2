# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
import feincms.module.medialibrary.fields


class Migration(migrations.Migration):

    dependencies = [
        ('medialibrary', '0002_auto_20201029_2041'),
        ('MainPagePomogut', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SocialReabilitation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('url', models.URLField(verbose_name='Ссылка')),
                ('title', models.CharField(verbose_name='название ссылки', max_length=25)),
                ('mediafile', feincms.module.medialibrary.fields.MediaFileForeignKey(verbose_name='Картинка', null=True, related_name='+', on_delete=django.db.models.deletion.SET_NULL, to='medialibrary.MediaFile')),
            ],
            options={
                'verbose_name': 'Сcылки для "Социальная реабилитация"',
                'verbose_name_plural': 'Сcылки для "Социальная реабилитация"',
            },
        ),
    ]
