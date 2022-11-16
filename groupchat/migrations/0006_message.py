# Generated by Django 3.2.15 on 2022-11-03 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groupchat', '0005_alter_groupchatmodel_group_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('context', models.TextField(blank=True, null=True)),
                ('sender', models.TextField(blank=True, null=True)),
                ('message', models.TextField(blank=True, null=True)),
                ('timestamp', models.DateTimeField(auto_now=True)),
                ('group', models.TextField(blank=True, null=True)),
                ('time', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
