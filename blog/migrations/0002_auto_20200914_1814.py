# Generated by Django 3.1.1 on 2020-09-14 12:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='slud',
            new_name='slug',
        ),
    ]
