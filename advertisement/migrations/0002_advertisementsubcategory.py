# Generated by Django 3.2.15 on 2022-11-16 07:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('advertisement', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdvertisementSubCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ads_subcategory', models.TextField()),
                ('ads_subcategory_discription', models.TextField()),
                ('ads_category_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='advertisement.advertismentcategory')),
            ],
        ),
    ]
