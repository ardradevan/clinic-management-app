# Generated by Django 4.2.6 on 2023-11-04 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('secondmini', '0005_alter_booking_p_email_alter_booking_p_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='p_email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='booking',
            name='p_name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='booking',
            name='p_phone',
            field=models.CharField(max_length=10),
        ),
    ]
