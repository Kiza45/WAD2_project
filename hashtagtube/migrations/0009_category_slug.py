# Generated by Django 2.2.17 on 2021-04-05 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hashtagtube', '0008_auto_20210331_1113'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(default=None, unique=True),
        ),
    ]