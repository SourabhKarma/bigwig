# Generated by Django 3.2.15 on 2022-10-19 10:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('groupchat', '0004_alter_groupchatmodel_text_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groupchatmodel',
            name='group_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='group_message', to='groupchat.groupmodel'),
        ),
    ]
