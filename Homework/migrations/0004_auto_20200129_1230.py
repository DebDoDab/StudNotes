# Generated by Django 3.0.2 on 2020-01-29 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Homework', '0003_unresolveddeadline'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deadline',
            name='expDate',
            field=models.DateField(verbose_name='date and time of expiration of a deadline'),
        ),
    ]