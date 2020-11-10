# Generated by Django 3.0 on 2020-11-07 17:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0015_auto_20201107_1956'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacancy',
            name='adress',
            field=models.TextField(blank=True, null=True, verbose_name='Адрес'),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cms.City', verbose_name='Город'),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='описание вакансии'),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='employer',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Работодаель'),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='ownership',
            field=models.CharField(blank=True, choices=[('1', 'Государственная'), ('2', 'Комерческая'), ('3', 'Общественная организация'), ('4', 'Религиозная организация')], max_length=64, null=True, verbose_name='тип оранизации'),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='position',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Позиция'),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='tel',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='Телефон'),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='time',
            field=models.CharField(blank=True, choices=[('1', 'Полная занятость'), ('2', 'Частичная занятость'), ('3', 'Подработка'), ('4', 'Гибкий график')], max_length=64, null=True, verbose_name='тип занятости'),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='title',
            field=models.CharField(max_length=256, verbose_name='Название'),
        ),
    ]