# Generated by Django 2.2.5 on 2020-08-31 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0002_auto_20200831_1918'),
    ]

    operations = [
        migrations.AddField(
            model_name='quotes',
            name='author',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='quotes',
            name='rating',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
