# Generated by Django 3.0 on 2020-10-19 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0024_auto_20201019_2054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newspage',
            name='template_key',
            field=models.CharField(choices=[('w1dget.html', 'Новость')], default='w1dget.html', max_length=255, verbose_name='template'),
        ),
    ]