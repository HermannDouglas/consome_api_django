# Generated by Django 4.2.2 on 2023-06-29 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_local_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='local',
            name='foto',
            field=models.URLField(null=True),
        ),
    ]
