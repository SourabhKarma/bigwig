# Generated by Django 3.2.15 on 2022-10-27 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0006_alter_storiesmodel_stories_end'),
    ]

    operations = [
        migrations.AddField(
            model_name='storiesmodel',
            name='view_count',
            field=models.IntegerField(default=0),
        ),
    ]
