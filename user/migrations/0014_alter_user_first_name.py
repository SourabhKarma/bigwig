# Generated by Django 3.2.15 on 2023-01-02 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0013_auto_20221115_1148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]
