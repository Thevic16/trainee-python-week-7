# Generated by Django 3.2 on 2022-03-10 03:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='gender',
            field=models.CharField(choices=[('other', 'Other'), ('feminine', 'Feminine'), ('male', 'Male')], max_length=120),
        ),
    ]