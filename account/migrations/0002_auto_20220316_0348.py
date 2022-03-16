# Generated by Django 3.2 on 2022-03-16 03:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myuser',
            name='is_staff',
        ),
        migrations.RemoveField(
            model_name='myuser',
            name='username',
        ),
        migrations.RemoveField(
            model_name='myuser',
            name='zipcode',
        ),
        migrations.AddField(
            model_name='myuser',
            name='date_of_birth',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
