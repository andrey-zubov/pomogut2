# Generated by Django 3.0 on 2020-11-08 10:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0034_calendararticle_link'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='calendararticle',
            name='bank_link',
        ),
    ]
