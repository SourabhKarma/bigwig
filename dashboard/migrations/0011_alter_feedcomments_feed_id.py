# Generated by Django 3.2.15 on 2022-10-12 07:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0010_delete_feedlikemodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedcomments',
            name='feed_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='feedcomments', to='dashboard.feedmodel'),
        ),
    ]
