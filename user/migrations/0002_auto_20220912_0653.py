# Generated by Django 3.2.15 on 2022-09-12 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='otp',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='ward',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
