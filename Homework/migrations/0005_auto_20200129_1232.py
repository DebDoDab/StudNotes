# Generated by Django 3.0.2 on 2020-01-29 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Homework', '0004_auto_20200129_1230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deadline',
            name='expDate',
            field=models.DateTimeField(verbose_name='date of expiration of a deadline'),
        ),
    ]
