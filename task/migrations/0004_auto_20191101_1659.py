# Generated by Django 2.0.5 on 2019-11-01 16:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0003_auto_20191101_1652'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='has_distribute',
            new_name='has_distributed',
        ),
        migrations.RenameField(
            model_name='task',
            old_name='has_finshed',
            new_name='has_finished',
        ),
    ]
