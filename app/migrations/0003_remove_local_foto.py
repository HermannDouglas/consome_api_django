# Generated by Django 4.2.2 on 2023-06-29 19:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_local_foto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='local',
            name='foto',
        ),
    ]
