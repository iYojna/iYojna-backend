# Generated by Django 4.1.2 on 2022-10-16 02:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0009_alter_user_dob_alter_user_educational_qualifications'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='educational_qualifications',
            field=models.IntegerField(choices=[(3, 'Graduate'), (2, 'Under Graduate'), (1, 'Schooling'), (0, 'Not Applicable')], default='Graduate'),
        ),
    ]
