# Generated by Django 5.1 on 2025-01-06 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("events", "0004_alter_eventregistration_registration_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="eventregistration",
            name="registration_date",
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
