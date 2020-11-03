# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_ymap.fields
import feincms.module.medialibrary.fields
import mptt.fields
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('medialibrary', '0001_initial'),
        ('page', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Block',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(verbose_name='Название блока', max_length=100)),
                ('slug', models.SlugField(verbose_name='Слаг')),
                ('name_button', models.CharField(verbose_name='Название кнопки', max_length=100)),
                ('text', models.TextField(verbose_name='Текст')),
            ],
            options={
                'verbose_name': 'Блок главной страницы',
                'verbose_name_plural': 'Блоки главной страницы',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(verbose_name='Название', max_length=50)),
                ('slug', models.SlugField(verbose_name='Слаг')),
                ('flag', models.BooleanField(verbose_name='Стадия разработки', default=False, help_text='Страницы будут не доступны для пользователя')),
                ('lft', models.PositiveIntegerField(db_index=True, editable=False)),
                ('rght', models.PositiveIntegerField(db_index=True, editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(db_index=True, editable=False)),
                ('mediafile', feincms.module.medialibrary.fields.MediaFileForeignKey(verbose_name='Картинка', blank=True, null=True, related_name='+', on_delete=django.db.models.deletion.SET_NULL, to='medialibrary.MediaFile')),
                ('parent', mptt.fields.TreeForeignKey(verbose_name='Родитель', blank=True, null=True, related_name='children', to='cms.Category')),
            ],
            options={
                'verbose_name': 'Раздел-категория-тег',
                'verbose_name_plural': 'Раздел-категория-тег',
                'db_table': 'category',
                'ordering': ('tree_id', 'level'),
            },
        ),
        migrations.CreateModel(
            name='Connect_with_us',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=20)),
                ('target_message', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('text', models.TextField()),
            ],
            options={
                'verbose_name': 'Форма обратной связи',
                'verbose_name_plural': 'Форма обратной связи',
            },
        ),
        migrations.CreateModel(
            name='Counter_children',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('couner1', models.IntegerField(default=0)),
                ('couner2', models.IntegerField(default=0)),
                ('couner3', models.IntegerField(default=0)),
                ('time', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name': 'Счетчик',
                'verbose_name_plural': 'Счетчик',
            },
        ),
        migrations.CreateModel(
            name='Encyclopedia_of_knowledge',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('request', models.CharField(verbose_name='Часто задаваемый вопрос', max_length=150)),
                ('response', models.TextField(verbose_name='Ответ:')),
            ],
            options={
                'verbose_name': 'Энциклопедия знаний',
                'verbose_name_plural': 'Энциклопедия знаний',
            },
        ),
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('request', models.CharField(verbose_name='Часто задаваемый вопрос', max_length=150)),
                ('response', models.TextField(verbose_name='Ответ:')),
            ],
            options={
                'verbose_name': 'FAQ',
            },
        ),
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('link', models.URLField(verbose_name='Ссылка')),
                ('title', models.CharField(verbose_name='название', max_length=150)),
            ],
            options={
                'verbose_name': 'Ссылка',
                'verbose_name_plural': 'Ссылки',
            },
        ),
        migrations.CreateModel(
            name='Map',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(verbose_name='Название точки', max_length=200)),
                ('description', models.TextField(verbose_name='описание точки')),
                ('address', django_ymap.fields.YmapCoord(max_length=200)),
            ],
            options={
                'verbose_name': 'Точка',
                'verbose_name_plural': 'Точки',
            },
        ),
        migrations.CreateModel(
            name='Relation_forarticle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('tite', models.CharField(verbose_name='название группы', max_length=150, blank=True, null=True)),
                ('pages', models.ManyToManyField(verbose_name='Статьи', help_text='<b>можно выбрать до 4-х статей.</b><br>', to='page.Page')),
            ],
            options={
                'verbose_name': 'Группа статей',
            },
        ),
        migrations.CreateModel(
            name='Search',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('word', models.CharField(max_length=100)),
                ('pages', models.ManyToManyField(to='page.Page')),
            ],
        ),
        migrations.AddField(
            model_name='block',
            name='categories',
            field=models.ManyToManyField(verbose_name='Раздел-категория-тег', to='cms.Category'),
        ),
        migrations.AddField(
            model_name='block',
            name='pages',
            field=models.ManyToManyField(verbose_name='Статьи', to='page.Page'),
        ),
        migrations.AddField(
            model_name='block',
            name='picture',
            field=feincms.module.medialibrary.fields.MediaFileForeignKey(verbose_name='Картинка', null=True, related_name='+', on_delete=django.db.models.deletion.SET_NULL, to='medialibrary.MediaFile'),
        ),
    ]
