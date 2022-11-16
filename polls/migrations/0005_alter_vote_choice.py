# Generated by Django 3.2.15 on 2022-10-03 09:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_alter_vote_voted_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vote',
            name='choice',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='votes', to='polls.choice'),
            preserve_default=False,
        ),
    ]
