# Generated by Django 3.2.15 on 2022-12-12 06:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0013_alter_eventlikemodel_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventlikemodel',
            name='eventid',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='event_count', to='events.eventmodel'),
        ),
    ]
