# Generated by Django 4.2.2 on 2023-06-28 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Local',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('rua', models.CharField(max_length=255)),
                ('numero', models.IntegerField()),
                ('foto', models.ImageField(blank=True, null=True, upload_to='locais')),
            ],
        ),
    ]