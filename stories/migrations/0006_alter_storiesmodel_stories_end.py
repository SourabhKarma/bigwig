# Generated by Django 3.2.15 on 2022-10-14 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0005_alter_storiesmodel_stories_start'),
    ]

    operations = [
        migrations.AlterField(
            model_name='storiesmodel',
            name='stories_end',
            field=models.DateField(blank=True, null=True),
        ),
    ]
