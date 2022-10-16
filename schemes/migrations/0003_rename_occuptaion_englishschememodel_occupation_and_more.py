# Generated by Django 4.1.2 on 2022-10-16 01:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schemes', '0002_remove_englishschememodel_extra_data_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='englishschememodel',
            old_name='occuptaion',
            new_name='occupation',
        ),
        migrations.RemoveField(
            model_name='englishschememodel',
            name='eduaction',
        ),
        migrations.AddField(
            model_name='englishschememodel',
            name='educational_qualifications',
            field=models.CharField(blank=True, choices=[('Graduate', 3), ('Under Graduate', 2), ('Schooling', 1), ('Not Applicable', 0)], max_length=15, null=True),
        ),
    ]
