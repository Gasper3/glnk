# Generated by Django 3.2.9 on 2021-12-04 10:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_auto_20211204_1016'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='LinkVisits',
            new_name='UrlVisits',
        ),
    ]
