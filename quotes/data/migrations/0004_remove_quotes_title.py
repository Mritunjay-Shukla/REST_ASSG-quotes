# Generated by Django 2.2.5 on 2020-08-31 13:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0003_auto_20200831_1923'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quotes',
            name='title',
        ),
    ]
