# Generated by Django 3.2.15 on 2022-11-03 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groupchat', '0007_auto_20221103_1056'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='groupInt',
            field=models.TextField(blank=True, null=True),
        ),
    ]
