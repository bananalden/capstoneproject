# Generated by Django 5.1.4 on 2025-03-17 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentprofile',
            name='address',
            field=models.CharField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='studentprofile',
            name='course',
            field=models.CharField(blank=True, null=True),
        ),
    ]
