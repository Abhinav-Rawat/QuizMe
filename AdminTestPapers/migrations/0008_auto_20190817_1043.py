# Generated by Django 2.2.4 on 2019-08-17 10:43

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('AdminTestPapers', '0007_auto_20190817_1042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 8, 17, 10, 43, 46, 457429, tzinfo=utc), verbose_name='date published'),
        ),
    ]
