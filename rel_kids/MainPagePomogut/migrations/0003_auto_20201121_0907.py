# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import feincms.module.medialibrary.fields
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('medialibrary', '0002_auto_20201029_2041'),
        ('MainPagePomogut', '0002_socialreabilitation'),
    ]

    operations = [
        migrations.CreateModel(
            name='MainPageBlock',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(verbose_name='Название направления', max_length=256)),
                ('text', models.TextField()),
                ('tel', models.CharField(verbose_name='Телефон', max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='MainPageLinks',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('url', models.URLField(verbose_name='Ссылка')),
                ('title', models.CharField(verbose_name='название ссылки', max_length=25)),
                ('block', models.ForeignKey(to='MainPagePomogut.MainPageBlock')),
                ('mediafile', feincms.module.medialibrary.fields.MediaFileForeignKey(verbose_name='Картинка', null=True, related_name='+', on_delete=django.db.models.deletion.SET_NULL, to='medialibrary.MediaFile')),
            ],
            options={
                'verbose_name': 'Сcылки для Блоков главной страницы',
                'verbose_name_plural': 'Сcылки для Блоков главной страницы',
            },
        ),
        migrations.RemoveField(
            model_name='socialreabilitation',
            name='mediafile',
        ),
        migrations.DeleteModel(
            name='SocialReabilitation',
        ),
    ]
