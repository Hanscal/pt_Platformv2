# Generated by Django 2.2.6 on 2020-05-28 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0003_dataitem_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dataitem',
            name='image',
            field=models.CharField(max_length=50, verbose_name='图片占位'),
        ),
        migrations.AlterField(
            model_name='dataitem',
            name='img_name',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='图片'),
        ),
    ]
