# Generated by Django 3.2.9 on 2021-12-01 19:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Url',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.TextField()),
                ('unique_id', models.TextField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='LinkVisits',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_address', models.CharField(max_length=15, null=True)),
                ('user_agent', models.CharField(max_length=255, null=True)),
                ('url', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='urls', to='main_app.url')),
            ],
        ),
    ]
