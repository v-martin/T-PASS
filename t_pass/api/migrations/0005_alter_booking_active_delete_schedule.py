# Generated by Django 5.0 on 2023-12-20 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_booking_options_booking_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.DeleteModel(
            name='Schedule',
        ),
    ]
