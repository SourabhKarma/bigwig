# Generated by Django 3.2.15 on 2022-09-30 07:51

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('polls', '0004_alter_vote_voted_by'),
        ('feedback', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='feedback',
            unique_together={('userid', 'pollsid')},
        ),
    ]
