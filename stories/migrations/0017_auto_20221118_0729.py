# Generated by Django 3.2.15 on 2022-11-18 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0016_item_image_urls'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='image_url',
            field=models.URLField(null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='image_urls',
            field=models.URLField(null=True),
        ),
    ]
