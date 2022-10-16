# Generated by Django 4.1.2 on 2022-10-16 02:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0010_alter_user_educational_qualifications'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='educational_qualifications',
        ),
        migrations.AddField(
            model_name='user',
            name='education',
            field=models.CharField(choices=[('Below 10th', 'Below 10th'), ('10th', '10th'), ('12th', '12th'), ('Graduate', 'Graduate'), ('Post Graduate', 'Post Graduate'), ('Doctorate', 'Doctorate')], default='Below 10th', max_length=20),
        ),
    ]