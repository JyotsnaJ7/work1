# Generated by Django 3.0 on 2020-10-20 10:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bdologin', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='followup',
            old_name='lead_Name',
            new_name='lead_name',
        ),
    ]
