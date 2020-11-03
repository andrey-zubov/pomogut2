# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import feincms.extensions.base
import feincms.translations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(verbose_name='title', max_length=200)),
                ('slug', models.SlugField(verbose_name='slug', max_length=150)),
                ('parent', models.ForeignKey(verbose_name='parent', blank=True, null=True, related_name='children', to='medialibrary.Category')),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
                'ordering': ['parent__title', 'title'],
            },
        ),
        migrations.CreateModel(
            name='MediaFile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('file', models.FileField(verbose_name='file', max_length=255, upload_to='medialibrary/%Y/%m/')),
                ('type', models.CharField(verbose_name='file type', max_length=12, editable=False, choices=[('image', 'Image'), ('video', 'Video'), ('audio', 'Audio'), ('pdf', 'PDF document'), ('swf', 'Flash'), ('txt', 'Text'), ('rtf', 'Rich Text'), ('zip', 'Zip archive'), ('doc', 'Microsoft Word'), ('xls', 'Microsoft Excel'), ('ppt', 'Microsoft PowerPoint'), ('other', 'Binary')])),
                ('created', models.DateTimeField(verbose_name='created', default=django.utils.timezone.now, editable=False)),
                ('file_size', models.IntegerField(verbose_name='file size', blank=True, null=True, editable=False)),
            ],
            bases=(models.Model, feincms.extensions.base.ExtensionsMixin, feincms.translations.TranslatedObjectMixin),
        ),
        migrations.CreateModel(
            name='MediaFileTranslation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('language_code', models.CharField(verbose_name='language', max_length=10, default='af', choices=[('af', 'Afrikaans'), ('ar', 'Arabic'), ('ast', 'Asturian'), ('az', 'Azerbaijani'), ('bg', 'Bulgarian'), ('be', 'Belarusian'), ('bn', 'Bengali'), ('br', 'Breton'), ('bs', 'Bosnian'), ('ca', 'Catalan'), ('cs', 'Czech'), ('cy', 'Welsh'), ('da', 'Danish'), ('de', 'German'), ('el', 'Greek'), ('en', 'English'), ('en-au', 'Australian English'), ('en-gb', 'British English'), ('eo', 'Esperanto'), ('es', 'Spanish'), ('es-ar', 'Argentinian Spanish'), ('es-mx', 'Mexican Spanish'), ('es-ni', 'Nicaraguan Spanish'), ('es-ve', 'Venezuelan Spanish'), ('et', 'Estonian'), ('eu', 'Basque'), ('fa', 'Persian'), ('fi', 'Finnish'), ('fr', 'French'), ('fy', 'Frisian'), ('ga', 'Irish'), ('gl', 'Galician'), ('he', 'Hebrew'), ('hi', 'Hindi'), ('hr', 'Croatian'), ('hu', 'Hungarian'), ('ia', 'Interlingua'), ('id', 'Indonesian'), ('io', 'Ido'), ('is', 'Icelandic'), ('it', 'Italian'), ('ja', 'Japanese'), ('ka', 'Georgian'), ('kk', 'Kazakh'), ('km', 'Khmer'), ('kn', 'Kannada'), ('ko', 'Korean'), ('lb', 'Luxembourgish'), ('lt', 'Lithuanian'), ('lv', 'Latvian'), ('mk', 'Macedonian'), ('ml', 'Malayalam'), ('mn', 'Mongolian'), ('mr', 'Marathi'), ('my', 'Burmese'), ('nb', 'Norwegian Bokmal'), ('ne', 'Nepali'), ('nl', 'Dutch'), ('nn', 'Norwegian Nynorsk'), ('os', 'Ossetic'), ('pa', 'Punjabi'), ('pl', 'Polish'), ('pt', 'Portuguese'), ('pt-br', 'Brazilian Portuguese'), ('ro', 'Romanian'), ('ru', 'Russian'), ('sk', 'Slovak'), ('sl', 'Slovenian'), ('sq', 'Albanian'), ('sr', 'Serbian'), ('sr-latn', 'Serbian Latin'), ('sv', 'Swedish'), ('sw', 'Swahili'), ('ta', 'Tamil'), ('te', 'Telugu'), ('th', 'Thai'), ('tr', 'Turkish'), ('tt', 'Tatar'), ('udm', 'Udmurt'), ('uk', 'Ukrainian'), ('ur', 'Urdu'), ('vi', 'Vietnamese'), ('zh-cn', 'Simplified Chinese'), ('zh-hans', 'Simplified Chinese'), ('zh-hant', 'Traditional Chinese'), ('zh-tw', 'Traditional Chinese')])),
                ('caption', models.CharField(verbose_name='caption', max_length=1000)),
                ('description', models.TextField(verbose_name='description', blank=True)),
                ('parent', models.ForeignKey(related_name='translations', to='medialibrary.MediaFile')),
            ],
            options={
                'verbose_name': 'media file translation',
                'verbose_name_plural': 'media file translations',
            },
        ),
        migrations.AlterUniqueTogether(
            name='mediafiletranslation',
            unique_together=set([('parent', 'language_code')]),
        ),
    ]
