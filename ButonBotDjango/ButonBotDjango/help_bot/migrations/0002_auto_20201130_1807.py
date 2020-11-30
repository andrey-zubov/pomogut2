# Generated by Django 3.0.8 on 2020-11-30 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('help_bot', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChatParam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='название сайта, справочное')),
                ('param', models.CharField(blank=True, help_text='пустой - показывает все корневые варианты чата, иначе abuse, kids, released и тд. Используется в родителях, в древе диалога', max_length=64, verbose_name='параметр')),
            ],
            options={
                'verbose_name': '_доступен на сайтах',
                'verbose_name_plural': '_доступен на сайтах',
            },
        ),
        migrations.AddField(
            model_name='needhelp',
            name='params',
            field=models.ManyToManyField(blank=True, help_text='выбор проектов, где будет отображен данный родитель', to='help_bot.ChatParam'),
        ),
    ]
