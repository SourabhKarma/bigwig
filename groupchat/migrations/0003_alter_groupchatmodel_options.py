# Generated by Django 3.2.15 on 2022-10-19 10:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('groupchat', '0002_groupchatmodel'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='groupchatmodel',
            options={'ordering': ['-text_time']},
        ),
    ]
