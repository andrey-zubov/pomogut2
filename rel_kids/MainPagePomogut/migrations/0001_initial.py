# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import feincms.module.medialibrary.fields
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('medialibrary', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactInformation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('phone', models.CharField(verbose_name='контактный телефон', max_length=17, blank=True, null=True)),
                ('email', models.EmailField(verbose_name='Адрес электронной почты', max_length=254, blank=True, null=True)),
                ('flag', models.BooleanField(verbose_name='отображать эту информацию', default=True)),
            ],
            options={
                'verbose_name': 'Контактная информация на сайте',
                'verbose_name_plural': 'Контактная информация на сайте',
            },
        ),
        migrations.CreateModel(
            name='Help_for_addicts_links',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('url', models.URLField(verbose_name='Ссылка')),
                ('title', models.CharField(verbose_name='название ссылки', max_length=25)),
                ('mediafile', feincms.module.medialibrary.fields.MediaFileForeignKey(verbose_name='Картинка', null=True, related_name='+', on_delete=django.db.models.deletion.SET_NULL, to='medialibrary.MediaFile')),
            ],
            options={
                'verbose_name': 'Сcылки для "Помощь наркозависимым"',
                'verbose_name_plural': 'Сcылки для "Помощь наркозависимым"',
                'db_table': 'Помощь наркозависимым',
            },
        ),
        migrations.CreateModel(
            name='Network_security_links',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('url', models.URLField(verbose_name='Ссылка')),
                ('title', models.CharField(verbose_name='название ссылки', max_length=25)),
                ('mediafile', feincms.module.medialibrary.fields.MediaFileForeignKey(verbose_name='Картинка', null=True, related_name='+', on_delete=django.db.models.deletion.SET_NULL, to='medialibrary.MediaFile')),
            ],
            options={
                'verbose_name': 'Ссылки для "Безопасность в сети"',
                'verbose_name_plural': 'Ссылки для "Безопасность в сети"',
                'db_table': 'Безопасность в сети',
            },
        ),
        migrations.CreateModel(
            name='Partners',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('link', models.CharField(verbose_name='Ссылка', max_length=100)),
                ('mediafile', feincms.module.medialibrary.fields.MediaFileForeignKey(verbose_name='Картинка', null=True, related_name='+', on_delete=django.db.models.deletion.SET_NULL, to='medialibrary.MediaFile')),
            ],
            options={
                'verbose_name': 'Партнер',
                'verbose_name_plural': 'Партнеры',
            },
        ),
        migrations.CreateModel(
            name='To_contact_us',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('email', models.EmailField(max_length=254)),
                ('text', models.TextField()),
            ],
            options={
                'verbose_name': 'Связаться с нами',
                'verbose_name_plural': 'Связаться с нами',
                'db_table': 'Связаться с нами',
            },
        ),
    ]
