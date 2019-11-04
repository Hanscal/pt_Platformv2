# Generated by Django 2.0.5 on 2019-11-02 12:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('task', '0005_dataitem'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='LabelTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('has_done', models.IntegerField(choices=[(0, '未标注'), (1, '跳过'), (2, '完成')], default=0, verbose_name='是否完成')),
                ('data_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='task.DataItem', verbose_name='数据')),
                ('tagger', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='标注者')),
            ],
            options={
                'verbose_name': '任务分配',
                'verbose_name_plural': '任务分配',
            },
        ),
    ]
