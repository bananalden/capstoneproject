# Generated by Django 5.1.4 on 2025-05-08 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0010_alter_transaction_payment_proof'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='payment_proof',
            field=models.ImageField(blank=True, null=True, upload_to='payment_proof/'),
        ),
    ]
