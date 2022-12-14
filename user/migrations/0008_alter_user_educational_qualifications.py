# Generated by Django 4.1.2 on 2022-10-16 01:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0007_user_tags"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="educational_qualifications",
            field=models.CharField(
                choices=[
                    ("Graduate", 3),
                    ("Under Graduate", 2),
                    ("Schooling", 1),
                    ("Not Applicable", 0),
                ],
                default="Graduate",
                max_length=15,
            ),
        ),
    ]
