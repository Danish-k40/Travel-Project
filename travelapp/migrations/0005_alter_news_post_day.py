# Generated by Django 3.2.6 on 2021-09-08 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0004_auto_20210826_1210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news_post',
            name='day',
            field=models.IntegerField(),
        ),
    ]