# Generated by Django 3.0 on 2020-10-19 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0021_articlepicture_newspage_richtextcontent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newspage',
            name='template_key',
            field=models.CharField(choices=[('base', 'Новость')], default='base', max_length=255, verbose_name='template'),
        ),
    ]
