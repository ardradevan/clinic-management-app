# Generated by Django 4.2.6 on 2023-11-03 17:37

from django.db import migrations, models
import secondmini.models


class Migration(migrations.Migration):

    dependencies = [
        ('secondmini', '0003_booking'),
    ]

    operations = [
        migrations.AlterField(
            model_name='departments',
            name='dep_name',
            field=models.CharField(max_length=100, validators=[secondmini.models.validate]),
        ),
    ]
