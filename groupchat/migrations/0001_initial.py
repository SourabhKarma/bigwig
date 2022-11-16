# Generated by Django 3.2.15 on 2022-10-18 08:25

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='GroupModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_name', models.CharField(blank=True, max_length=100, null=True)),
                ('group_members', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
