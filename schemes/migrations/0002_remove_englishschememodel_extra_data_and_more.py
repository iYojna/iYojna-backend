# Generated by Django 4.1.2 on 2022-10-15 17:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("schemes", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="englishschememodel",
            name="extra_data",
        ),
        migrations.RemoveField(
            model_name="gujschememodel",
            name="extra_data",
        ),
    ]
