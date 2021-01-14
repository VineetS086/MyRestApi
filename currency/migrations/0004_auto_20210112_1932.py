# Generated by Django 3.1.4 on 2021-01-12 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('currency', '0003_auto_20210112_1258'),
    ]

    operations = [
        migrations.AddField(
            model_name='currency',
            name='update_status',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='currency',
            name='value',
            field=models.DecimalField(decimal_places=8, default=1.0, max_digits=25),
        ),
    ]