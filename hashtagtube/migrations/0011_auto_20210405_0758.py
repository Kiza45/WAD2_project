# Generated by Django 2.2.17 on 2021-04-05 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hashtagtube', '0010_auto_20210405_0734'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(),
        ),
    ]