# Generated by Django 3.2.15 on 2022-09-19 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='videomodel',
            name='title',
            field=models.BinaryField(blank=True, null=True),
        ),
    ]
