# Generated by Django 3.0.2 on 2020-01-29 10:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Homework', '0002_auto_20200128_2036'),
    ]

    operations = [
        migrations.CreateModel(
            name='UnresolvedDeadline',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deadlineId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Homework.Deadline')),
                ('userId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Homework.User')),
            ],
        ),
    ]
